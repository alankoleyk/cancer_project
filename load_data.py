# load_data.py
# Reads the CSV and splits it into training and testing sets.
import csv
import random


def load_patients(filename):
    """Read the CSV and return a list of patients.
    Each patient is a tuple: (therapy_combo, survived)
    therapy_combo is (hormone, chemo, radio), each 0 or 1.
    survived is 1 if the patient lived, 0 if not."""
    patients = []
    file = open(filename)
    reader = csv.DictReader(file)
    for row in reader:
        hormone = int(row["hormone_therapy"])
        chemo = int(row["chemotherapy"])
        radio = int(row["radio_therapy"])
        survived = int(row["overall_survival"])
        combo = (hormone, chemo, radio)
        patients.append((combo, survived))
    file.close()
    return patients


def split_data(patients, train_fraction=0.8):
    """Shuffle the patients, then use the first 80% for training
    and the last 20% for testing."""
    random.seed(42)  # same shuffle every run, so results can be repeated
    random.shuffle(patients)
    cutoff = int(len(patients) * train_fraction)
    train = patients[:cutoff]
    test = patients[cutoff:]
    return train, test
