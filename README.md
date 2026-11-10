# Spanish Electricity Demand Forecasting with a Heterogeneous Ensemble

An academic team project investigating whether a heterogeneous ensemble can improve hour-ahead electricity-demand forecasts for Spain.

![Forecast and actual demand](reports/figures/fig9_forecast_vs_actual.png)

## Overview

Accurate short-term electricity-demand forecasts help system operators balance supply and demand, schedule generation and manage system reliability. This project compares several statistical and machine-learning models under a chronological evaluation design and combines their predictions in an optimised weighted ensemble.

The project uses hourly Spanish energy-system data and weather observations from 2015 to 2018. The prediction target is **total electricity load**, measured in MWh.

## Research question

Can a weighted ensemble of diverse forecasting models outperform its individual components when predicting Spanish hourly electricity demand?

## Data

- **Period:** 2015–2018
- **Frequency:** hourly
- **Energy observations:** 35,064 hours
- **Inputs:** historical electricity load, calendar variables, lagged features and weather observations
- **Weather coverage:** five Spanish cities
- **Target:** total load actual (MWh)

The two source files come from the Kaggle dataset [Hourly energy demand, generation and weather](https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather). Raw data are not committed to this repository; see [`data/README.md`](data/README.md) for download and placement instructions.

## Models

The analysis compares a seasonal naive benchmark with seven individual models:

1. Ridge regression
2. K-nearest neighbours
3. Linear support vector regression
4. Random forest
5. Gradient boosting
6. XGBoost
7. Multilayer perceptron

An additional ensemble chooses non-negative model weights by minimising validation error.

## Evaluation

The data are divided chronologically to avoid using future observations to predict the past. Performance is evaluated using RMSE, MAE, MAPE and R².

### Main results

| Model | Test RMSE (MWh) | Test MAE (MWh) | Test MAPE | Test R² |
|---|---:|---:|---:|---:|
| Optimised ensemble | **531.84** | **319.71** | **1.12%** | **0.9866** |
| XGBoost | 534.88 | 329.86 | 1.17% | 0.9865 |
| Random forest | 542.09 | 327.97 | 1.15% | 0.9861 |
| Gradient boosting | 590.29 | 383.38 | 1.35% | 0.9835 |
| Heuristic ensemble | 621.51 | 406.81 | 1.41% | 0.9818 |
| MLP | 724.80 | 493.41 | 1.75% | 0.9752 |
| Simple-average ensemble | 975.85 | 725.40 | 2.40% | 0.9550 |
| Ridge regression | 1,013.10 | 749.36 | 2.56% | 0.9515 |
| KNN | 2,047.98 | 1,457.51 | 5.07% | 0.8020 |
| Seasonal naive (t−24) | 3,588.55 | 2,519.00 | 8.74% | 0.3920 |
| Linear SVR | 4,170.71 | 3,553.37 | 11.48% | 0.1787 |

The optimised ensemble achieved the best result across all four reported test metrics. Its RMSE improvement over XGBoost—the strongest individual model by RMSE—was modest, so the result should be interpreted as an incremental forecasting gain rather than evidence that ensembling always dominates a strong individual learner.

![Test RMSE comparison](reports/figures/fig7_rmse_comparison.png)

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── electricity_demand_forecasting.ipynb
├── reports/
│   └── figures/
├── results/
│   └── results_table.csv
└── data/
    └── README.md
```

The notebook contains the complete course-project workflow. A future version may refactor repeated operations into reusable modules, but the current release prioritises transparency and fidelity to the submitted analysis.

## Reproducibility

After downloading the two source files, the workflow is:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Open `notebooks/electricity_demand_forecasting.ipynb` and run the cells from top to bottom. The notebook expects both CSV files in `data/raw/`.

The complete notebook was re-executed from a clean copy on 10 November 2026 using Python 3.13 and the pinned dependencies in `requirements.txt`. All 45 code cells completed without errors, and the resulting metrics and figures were used to update this repository.

## Limitations

- The analysis covers a single country and historical period.
- Weather observations from five cities may not fully represent national conditions.
- Hyperparameter selection is constrained by the computational scope of a course project.
- Performance should be reassessed on more recent data and under rolling-origin validation.
- The ensemble's gain over XGBoost is small and may not persist in a different period.

## Team and attribution

Developed as a Machine Learning course project by:

- Didac Bustamante
- Nil Castaño
- Taiki Causton
- Joan Garcia Almenara

This was a collaborative course project. Individual contributions will be described once they have been confirmed with the team.

The data-cleaning and exploratory structure was informed by Dimitrios Roussis's Kaggle notebook [Electricity price forecasting with DNNs (+ EDA)](https://www.kaggle.com/code/dimitriosroussis/electricity-price-forecasting-with-dnns-eda), released under the Apache 2.0 licence. This project changes the target from electricity price to electricity demand and uses a distinct modelling and ensemble strategy. See [`ATTRIBUTION.md`](ATTRIBUTION.md).

## Status

This repository is being prepared for public release. Team approval and individual contribution statements are still pending.

