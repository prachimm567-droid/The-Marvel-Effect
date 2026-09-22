# The Marvel Effect — Audience Engagement Prediction

A gamified Marvel personality-matching application using scenario-based user choices and supervised machine learning.

## What changed in this version

This version addresses the ML evaluation requirements:

- Expanded training dataset: **3,000 synthetic samples**
- 10 personality features
- 10 Marvel character classes
- Stratified **80/20 train-test split**
- Three classification models trained separately:
  - K-Nearest Neighbors (KNN)
  - Decision Tree
  - Logistic Regression
- Accuracy, macro Precision, macro Recall, and macro F1 calculated for every model
- Models compared on the **same held-out test set**
- Final model selected using the highest macro F1 score
- Final model saved and used directly by the Streamlit application
- Confusion matrix and classification reports saved in `results/`

## Dataset methodology

`data/characters.csv` contains one engineered reference profile per character. It is a prototype reference dataset, not a scientifically validated psychological dataset.

`data/generate_dataset.py` creates 300 controlled synthetic variations around each reference profile. Values remain on the project's 1–10 feature scale. The generated dataset is shuffled before training.

The synthetic nature of the dataset must be stated in the project presentation/report. Model performance describes performance on this controlled synthetic dataset and should **not** be interpreted as real-world psychological accuracy.

## ML workflow

```text
Scenario choices
      ↓
10 personality features
      ↓
Training dataset
      ↓
80/20 stratified split
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

## Results included with this package

The `results/` folder contains:

- `model_comparison.csv` — overall comparison of the three models
- `classification_report_*.csv` — class-level precision, recall, F1 and support
- `confusion_matrix_final.png` — confusion matrix for the selected final model
- `final_model_test_predictions.csv` — predictions made on the held-out test set
- `training_metadata.json` — split, selection and dataset metadata

The trained model is stored as:

```text
model/final_model.joblib
```

## Important interpretation note

The application predicts the character class represented by the project's engineered/synthetic training data. Its confidence values are model outputs, not clinical or psychological measurements.
