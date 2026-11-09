"""Prepare the submitted course notebook for a public repository.

This script removes internal drafting notes, replaces the unverified opening
context, updates paths to match the repository structure, and clears stored
outputs so the public notebook has no stale or contradictory execution state.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


OPENING = """# Spanish Electricity Demand Forecasting with a Heterogeneous Ensemble

**UPF Machine Learning course project · 2026**

**Authors:** Didac Bustamante, Nil Castaño, Taiki Causton and Joan Garcia Almenara

This notebook investigates hour-ahead electricity-demand forecasting for Spain
using hourly energy-system and weather data from 2015 to 2018. It compares a
seasonal naive benchmark with seven statistical and machine-learning models and
then combines their forecasts using heterogeneous ensembles.

The target is `total load actual`, measured in MWh. Price variables are excluded
because this project forecasts physical electricity demand rather than market
prices.

## Data and attribution

The two CSV files come from the Kaggle dataset [Hourly energy demand, generation
and weather](https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather).
Place them in `data/raw/` as described in the repository's data README.

The data-cleaning and exploratory structure was informed by Dimitrios Roussis's
[Electricity price forecasting with DNNs (+ EDA)](https://www.kaggle.com/code/dimitriosroussis/electricity-price-forecasting-with-dnns-eda),
released under the Apache 2.0 licence. This project changes the prediction target,
feature engineering, model comparison and ensemble methodology.
"""


ENVIRONMENT = """## Environment

Install the dependencies from the repository root before running the notebook:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
"""


def markdown_cell(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.rstrip().splitlines()],
    }


def prepare(source: Path, destination: Path) -> None:
    notebook = json.loads(source.read_text(encoding="utf-8"))
    cleaned_cells = []

    for index, cell in enumerate(notebook["cells"]):
        text = "".join(cell.get("source", []))

        if index == 0:
            cleaned_cells.append(markdown_cell(OPENING))
            continue

        if cell.get("cell_type") == "code" and "%pip install" in text:
            cleaned_cells.append(markdown_cell(ENVIRONMENT))
            continue

        if "AIXO HO HE AFEGIT JO" in text:
            continue

        if text.startswith("En aquest cas a diferencia"):
            continue

        if cell.get("cell_type") == "code":
            replacements = {
                'pd.read_csv("energy_dataset.csv"': 'pd.read_csv("../data/raw/energy_dataset.csv"',
                'pd.read_csv("weather_features.csv"': 'pd.read_csv("../data/raw/weather_features.csv"',
                'os.makedirs("figures"': 'os.makedirs("../reports/figures"',
                '"figures/': '"../reports/figures/',
                'to_csv("results_table.csv"': 'to_csv("../results/results_table.csv"',
            }
            for old, new in replacements.items():
                text = text.replace(old, new)
            cell["source"] = [line + "\n" for line in text.rstrip().splitlines()]
            cell["outputs"] = []
            cell["execution_count"] = None

        cleaned_cells.append(cell)

    notebook["cells"] = cleaned_cells
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    prepare(args.source, args.destination)


if __name__ == "__main__":
    main()
