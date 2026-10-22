# model.py
# A very simple "model": for each therapy combination, count how many
# training patients survived. Predict whichever outcome was more common.


def train_model(train_patients):
    """Returns a dictionary: combo -> [number_died, number_survived]"""
    counts = {}
    for combo, survived in train_patients:
        if combo not in counts:
            counts[combo] = [0, 0]
        counts[combo][survived] += 1
    return counts


def predict(model, combo):
    """Predict 1 (survives) or 0 (does not) for a therapy combination."""
    if combo not in model:
        return 0  # never seen in training; fall back to a default guess
    died, lived = model[combo]
    if lived > died:
        return 1
    return 0


def survival_rate(model, combo):
    """Fraction of training patients with this combo who survived."""
    died, lived = model[combo]
    return lived / (died + lived)
