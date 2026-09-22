from pathlib import Path
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
PROFILE_FILE = BASE / "data" / "characters.csv"
OUTPUT_FILE = BASE / "data" / "training_dataset.csv"

FEATURES = [
    "empathy", "leadership", "loyalty", "risk_taking",
    "strategic_thinking", "independence", "impulsiveness",
    "moral_reasoning", "humor", "self_sacrifice"
]

SAMPLES_PER_CHARACTER = 300
NOISE_STD = 1.25
RANDOM_STATE = 42


def build_dataset():
    profiles = pd.read_csv(PROFILE_FILE)
    rng = np.random.default_rng(RANDOM_STATE)
    rows = []

    for _, profile in profiles.iterrows():
        center = profile[FEATURES].astype(float).to_numpy()
        for _ in range(SAMPLES_PER_CHARACTER):
            # Controlled variation around each engineered reference profile.
            # Values are clipped to the project's 1-10 trait scale.
            sample = np.clip(
                center + rng.normal(0, NOISE_STD, size=len(FEATURES)),
                1,
                10,
            )
            rows.append([*sample, profile["character"]])

    dataset = pd.DataFrame(rows, columns=FEATURES + ["character"])
    dataset = dataset.sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
    dataset.to_csv(OUTPUT_FILE, index=False)

    print(f"Generated {len(dataset):,} samples.")
    print(f"Characters: {dataset['character'].nunique()}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_dataset()
