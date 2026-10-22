# main.py
# Run this file:  python main.py
from load_data import load_patients, split_data
from model import train_model, predict, survival_rate
from evaluate import accuracy, baseline_accuracy
from visualize import combo_name, plot_survival_rates, plot_accuracy, plot_test_results

FILENAME = "data/METABRIC_RNA_Mutation.csv"


patients = load_patients(FILENAME)
train, test = split_data(patients)
print("Patients:", len(patients), "| train:", len(train), "| test:", len(test))

model = train_model(train)

print("\nLearned from training data:")
for combo in sorted(model):
    died, lived = model[combo]
    print(f"  {combo_name(combo):28s} n={died + lived:4d}  "
          f"survival rate={survival_rate(model, combo):.0%}  "
          f"-> predict {'survives' if predict(model, combo) else 'does not survive'}")

model_acc = accuracy(model, test)
baseline_acc = baseline_accuracy(train, test)
print("\nTest accuracy:     ", round(model_acc, 3))
print("Baseline accuracy: ", round(baseline_acc, 3),
      "(always guessing the most common outcome)")

plot_survival_rates(model)
plot_accuracy(model_acc, baseline_acc)
plot_test_results(model, test)
print("\nSaved graphs: survival_by_therapy.png, accuracy.png, test_results.png")