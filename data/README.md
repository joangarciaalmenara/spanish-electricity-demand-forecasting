# Data setup

The raw data are not stored in this repository.

## Source

Download the dataset **Hourly energy demand, generation and weather** from Kaggle:

<https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather>

The project uses:

- `energy_dataset.csv`
- `weather_features.csv`

The energy data contain 35,064 hourly observations for Spain from 2015 through 2018. Weather observations cover Barcelona, Bilbao, Madrid, Seville and Valencia.

## Expected local structure

After downloading and extracting the dataset, place the files here:

```text
data/
└── raw/
    ├── energy_dataset.csv
    └── weather_features.csv
```

The `data/raw/` directory is ignored by Git so the source files are not committed accidentally.

## Provenance

According to the dataset documentation, the electricity-system variables originate from ENTSO-E, and the weather observations originate from the OpenWeather API. Consult the Kaggle dataset page and the original providers for the current terms and attribution requirements.

