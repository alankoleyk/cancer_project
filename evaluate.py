# evaluate.py
# Measures how accurate the model is on the test set.
from model import predict


def accuracy(model, test_patients):
    correct = 0
    for combo, survived in test_patients:
        if predict(model, combo) == survived:
            correct += 1
    return correct / len(test_patients)


def baseline_accuracy(train_patients, test_patients):
    """What if we ignored therapy and always guessed the most common outcome?
    This is the number the model needs to beat."""
    lived = 0
    for combo, survived in train_patients:
        lived += survived
    guess = 1 if lived > len(train_patients) / 2 else 0

    correct = 0
    for combo, survived in test_patients:
        if survived == guess:
            correct += 1
    return correct / len(test_patients)
