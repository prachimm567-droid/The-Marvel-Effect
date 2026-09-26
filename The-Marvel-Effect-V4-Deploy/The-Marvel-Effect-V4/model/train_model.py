from pathlib import Path
import json
import re

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

BASE = Path(__file__).resolve().parents[1]
DATA_FILE = BASE / "data" / "training_dataset.csv"
RESULTS_DIR = BASE / "results"
MODEL_DIR = BASE / "model"

FEATURES = [
    "empathy", "leadership", "loyalty", "risk_taking",
    "strategic_thinking", "independence", "impulsiveness",
    "moral_reasoning", "humor", "self_sacrifice"
]
TARGET = "character"
RANDOM_STATE = 42
TEST_SIZE = 0.20


def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def build_models():
    return {
        "KNN": Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", KNeighborsClassifier(n_neighbors=7)),
        ]),
        "Decision Tree": DecisionTreeClassifier(
            max_depth=8,
            min_samples_leaf=3,
            random_state=RANDOM_STATE,
        ),
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(
                max_iter=3000,
                random_state=RANDOM_STATE,
            )),
        ]),
    }


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    data = pd.read_csv(DATA_FILE)
    X = data[FEATURES]
    y = data[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    print("=" * 70)
    print("THE MARVEL EFFECT — MODEL TRAINING")
    print("=" * 70)
    print(f"Dataset: {len(data):,} rows")
    print(f"Features: {len(FEATURES)}")
    print(f"Classes: {y.nunique()}")
    print(f"Training samples: {len(X_train):,}")
    print(f"Testing samples: {len(X_test):,}")
    print("Split: 80% train / 20% test, stratified, random_state=42")

    rows = []
    fitted_models = {}

    for name, model in build_models().items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)

        accuracy = accuracy_score(y_test, prediction)
        precision = precision_score(y_test, prediction, average="macro", zero_division=0)
        recall = recall_score(y_test, prediction, average="macro", zero_division=0)
        f1 = f1_score(y_test, prediction, average="macro", zero_division=0)

        rows.append({
            "model": name,
            "accuracy": accuracy,
            "precision_macro": precision,
            "recall_macro": recall,
            "f1_macro": f1,
        })
        fitted_models[name] = model

        report = pd.DataFrame(
            classification_report(
                y_test,
                prediction,
                output_dict=True,
                zero_division=0,
            )
        ).transpose()
        report.to_csv(RESULTS_DIR / f"classification_report_{slug(name)}.csv")

        print(
            f"Accuracy={accuracy:.4f} | Precision={precision:.4f} | "
            f"Recall={recall:.4f} | F1={f1:.4f}"
        )

    comparison = pd.DataFrame(rows).sort_values(
        ["f1_macro", "accuracy", "precision_macro", "recall_macro"],
        ascending=False,
    ).reset_index(drop=True)
    comparison.insert(0, "rank", range(1, len(comparison) + 1))
    comparison.to_csv(RESULTS_DIR / "model_comparison.csv", index=False)

    # Final model: highest macro F1 on the common held-out test set.
    final_name = comparison.iloc[0]["model"]
    final_model = fitted_models[final_name]
    joblib.dump(final_model, MODEL_DIR / "final_model.joblib")

    final_prediction = final_model.predict(X_test)
    labels = sorted(y.unique())
    cm = confusion_matrix(y_test, final_prediction, labels=labels)

    fig, ax = plt.subplots(figsize=(11, 9))
    image = ax.imshow(cm)
    ax.set_title(f"Confusion Matrix — Final Model: {final_name}")
    ax.set_xlabel("Predicted Character")
    ax.set_ylabel("True Character")
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(labels, fontsize=8)
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, cm[i, j], ha="center", va="center", fontsize=7)
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / "confusion_matrix_final.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    test_output = X_test.copy()
    test_output[TARGET] = y_test.values
    test_output["predicted_character"] = final_prediction
    test_output.to_csv(RESULTS_DIR / "final_model_test_predictions.csv", index=False)

    metadata = {
        "dataset_rows": int(len(data)),
        "features": FEATURES,
        "target": TARGET,
        "classes": sorted(y.unique().tolist()),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "test_size": TEST_SIZE,
        "random_state": RANDOM_STATE,
        "selection_metric": "macro_f1",
        "final_model": final_name,
        "data_type": "synthetic controlled variation around engineered character reference profiles",
        "note": "Metrics describe performance on this synthetic dataset and should not be interpreted as psychological accuracy.",
    }
    with open(RESULTS_DIR / "training_metadata.json", "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=2)

    print("\n" + "=" * 70)
    print(f"FINAL MODEL: {final_name}")
    print("Selection criterion: highest macro F1 on the common 20% test set")
    print("Saved: model/final_model.joblib")
    print("Saved: results/model_comparison.csv")
    print("Saved: results/confusion_matrix_final.png")
    print("=" * 70)


if __name__ == "__main__":
    main()
