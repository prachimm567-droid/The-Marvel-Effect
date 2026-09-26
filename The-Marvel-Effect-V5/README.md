# The Marvel Effect — V5

Gamified Marvel character personality prediction using synthetic training data and three ML classifiers.

## Streamlit Community Cloud

**Main file path:**

`The-Marvel-Effect-V5/app/app.py`

The dependency file is intentionally placed beside the Streamlit entrypoint:

`The-Marvel-Effect-V5/app/requirements.txt`

This file contains all external packages required by the app, including `joblib`.

## Local run

```bash
pip install -r app/requirements.txt
python -m streamlit run app/app.py
```

## ML setup

If the pre-trained model is present, launch the app directly. To regenerate the synthetic dataset and model:

```bash
python data/generate_dataset.py
python model/train_model.py
python -m streamlit run app/app.py
```

## Academic note

The training data is synthetic and the character trait profiles are engineered reference values for an academic demonstration. Model metrics describe performance on this synthetic dataset and are not validated psychological measurements.
