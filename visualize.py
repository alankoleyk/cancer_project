# visualize.py
# Makes simple graphs and saves them as PNG pictures.
import matplotlib
matplotlib.use("Agg")  # lets us save pictures without opening a window
import matplotlib.pyplot as plt

from model import predict, survival_rate


def combo_name(combo):
    names = ["hormone", "chemo", "radio"]
    parts = []
    for i in range(3):
        if combo[i] == 1:
            parts.append(names[i])
    if len(parts) == 0:
        return "no therapy"
    return " + ".join(parts)


def plot_survival_rates(model, filename="survival_by_therapy.png"):
    """Bar chart: survival rate for each therapy combination."""
    combos = sorted(model, key=lambda c: survival_rate(model, c))
    labels = []
    rates = []
    colors = []
    for combo in combos:
        died, lived = model[combo]
        labels.append(combo_name(combo) + "\n(n=" + str(died + lived) + ")")
        rate = survival_rate(model, combo)
        rates.append(rate * 100)
        if predict(model, combo) == 1:
            colors.append("green")
        else:
            colors.append("red")

    plt.figure(figsize=(10, 6))
    plt.barh(labels, rates, color=colors)
    plt.axvline(50, color="black", linestyle="--")  # 50% line
    plt.xlabel("Survival rate in training data (%)")
    plt.title("Survival rate by therapy combination\n"
              "(green = model predicts survives, red = predicts does not)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_accuracy(model_acc, baseline_acc, filename="accuracy.png"):
    """Bar chart: model accuracy vs. the always-guess-the-same baseline."""
    plt.figure(figsize=(5, 5))
    plt.bar(["Baseline", "Model"], [baseline_acc * 100, model_acc * 100],
            color=["gray", "blue"])
    plt.ylim(0, 100)
    plt.ylabel("Test accuracy (%)")
    plt.title("Model vs. baseline")
    plt.text(0, baseline_acc * 100 + 1, str(round(baseline_acc * 100, 1)) + "%", ha="center")
    plt.text(1, model_acc * 100 + 1, str(round(model_acc * 100, 1)) + "%", ha="center")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_test_results(model, test_patients, filename="test_results.png"):
    """Grouped bars: for each combo, how many test patients the model got
    right and wrong."""
    right = {}
    wrong = {}
    for combo in model:
        right[combo] = 0
        wrong[combo] = 0
    for combo, survived in test_patients:
        if predict(model, combo) == survived:
            right[combo] += 1
        else:
            wrong[combo] += 1

    combos = sorted(model)
    labels = []
    right_counts = []
    wrong_counts = []
    for combo in combos:
        labels.append(combo_name(combo))
        right_counts.append(right[combo])
        wrong_counts.append(wrong[combo])

    positions = list(range(len(combos)))
    left_positions = []
    right_positions = []
    for p in positions:
        left_positions.append(p - 0.2)
        right_positions.append(p + 0.2)

    plt.figure(figsize=(10, 6))
    plt.bar(left_positions, right_counts, width=0.4, color="green", label="Correct")
    plt.bar(right_positions, wrong_counts, width=0.4, color="red", label="Wrong")
    plt.xticks(positions, labels, rotation=30, ha="right")
    plt.ylabel("Number of test patients")
    plt.title("Test predictions by therapy combination")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
