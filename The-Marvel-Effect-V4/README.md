# The Marvel Effect — Audience Engagement Prediction

A gamified Marvel character prediction application using scenario-based user choices and supervised machine learning.

## Final ML version

This version expands the original prototype and addresses the requested ML improvements:

- **25 Marvel character classes**
- **7,500 synthetic training samples**
- 10 personality/behavior features
- Balanced **300 samples per character**
- Stratified **80/20 train-test split**
- 6,000 training samples and 1,500 held-out test samples
- Three independently trained classification models:
  - K-Nearest Neighbors (KNN)
  - Decision Tree
  - Logistic Regression
- Accuracy, macro Precision, macro Recall and macro F1 for every model
- Same held-out test set used for fair comparison
- Final model selected using the highest macro F1-score
- Final trained model saved for Streamlit inference
- Per-class classification reports and final confusion matrix saved in `results/`

## Character classes

The current dataset contains 25 engineered reference profiles:

Tony Stark, Steve Rogers, Thor, Peter Parker, Natasha Romanoff, Wanda Maximoff, Doctor Strange, Shuri, T'Challa / Black Panther, Sam Wilson, Bucky Barnes, Carol Danvers, Scott Lang, Shang-Chi, Kamala Khan, Loki, Yelena Belova, Deadpool, Moon Knight, Venom / Eddie Brock, Thanos, Killmonger, Doctor Doom, Magneto, and Green Goblin.

## Dataset methodology

`data/characters.csv` contains one engineered reference profile per character. These values are project-defined reference values and are **not scientifically validated psychological measurements**.

`data/generate_dataset.py` creates 300 controlled synthetic variations around each reference profile. Values remain on the project's 1–10 feature scale. The generated dataset is shuffled before training.

The dataset is synthetic and does not represent real users. Model performance therefore describes performance on this controlled experimental dataset and should not be interpreted as real-world psychological prediction accuracy.

## ML workflow

```text
Scenario choices
      ↓
10 personality features
      ↓
7,500-sample synthetic training dataset
      ↓
80/20 stratified train-test split
      ↓
 ┌───────────────┬────────────────┬────────────────────┐
 │      KNN      │  Decision Tree │ Logistic Regression │
 └───────────────┴────────────────┴────────────────────┘
      ↓
Accuracy / Precision / Recall / F1
      ↓
Model comparison
      ↓
Final model selected by macro F1
      ↓
Streamlit prediction
```

## Final experiment results

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 |
|---|---:|---:|---:|---:|
| KNN | 66.53% | 66.35% | 66.53% | 66.05% |
| Decision Tree | 49.33% | 50.43% | 49.33% | 49.27% |
| Logistic Regression | **73.20%** | **73.25%** | **73.20%** | **73.04%** |

**Final model: Logistic Regression**, selected because it achieved the highest macro F1-score on the common held-out test set.

## Run the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Regenerate the dataset if needed:

```bash
python data/generate_dataset.py
```

Train and evaluate all models:

```bash
python model/train_model.py
```

Launch the application:

```bash
python -m streamlit run app/app.py
```

## Results included

The `results/` folder contains:

- `model_comparison.csv` — comparison of all three models
- `classification_report_knn.csv` — detailed KNN report
- `classification_report_decision_tree.csv` — detailed Decision Tree report
- `classification_report_logistic_regression.csv` — detailed Logistic Regression report
- `confusion_matrix_final.png` — confusion matrix for the selected final model
- `final_model_test_predictions.csv` — predictions on the held-out test set
- `training_metadata.json` — experiment metadata

The trained model is stored as:

```text
model/final_model.joblib
```

## Scenario scoring

The scenario engine uses positive and negative trait contributions rather than only increasing scores. Trait values are clipped to the 1–10 range before inference. This broadens the reachable feature space compared with the original prototype.

## Important interpretation note

The application is an educational/entertainment ML demonstration. Its predicted character and model confidence values are outputs of the trained classifier and are not psychological diagnoses or scientifically validated personality measurements.
