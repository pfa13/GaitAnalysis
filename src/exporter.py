import csv
import os

class Exporter:
    def save_to_csv(self, results, filename="results/metrics.csv"):
        os.makedirs("results", exist_ok=True)

        keys = results[0].keys()

        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)

        print(f"Results saved to {filename}")