# Attribution

## Source data

The project uses the Kaggle dataset [Hourly energy demand, generation and weather](https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather), uploaded by Nicholas Jhana.

The repository does not redistribute the raw CSV files. Users are directed to the source page to obtain the data and review its terms.

## Prior notebook

Parts of the data-cleaning and exploratory workflow were informed by:

> Dimitrios Roussis, [Electricity price forecasting with DNNs (+ EDA)](https://www.kaggle.com/code/dimitriosroussis/electricity-price-forecasting-with-dnns-eda), Kaggle, version 28. Released under the Apache 2.0 licence.

The present project differs materially in its research question and modelling strategy:

- it predicts `total load actual` rather than electricity price;
- it removes price variables from the feature set;
- it introduces demand-specific temporal, lag, holiday, rolling and temperature features;
- it compares seven statistical and machine-learning models;
- it constructs and evaluates several heterogeneous ensembles.

## Academic team

- Didac Bustamante
- Nil Castaño
- Taiki Causton
- Joan Garcia Almenara

The repository will only be made public after the team attribution and publication decision have been confirmed.

