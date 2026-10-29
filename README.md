# Climate Change Analysis Project
## Exploring Forty Years of Weather Across Contrasting Environments

### Project Overview

This is my Python project for studying how weather conditions have changed across different climate environments between 1986 and 2025.

I started by testing the Open-Meteo Historical Weather API with three locations. Later, I decided to organize the project using the Köppen–Geiger climate classification, selecting two locations from each of the five major climate groups.

The goal is to investigate long-term temperature changes, compare locations within the same climate group, and explore how apparent temperature, humidity and sunshine duration vary across different environments.

### Locations

| Climate group | Locations |
|---|---|
| A — Tropical | Kisangani, Darwin |
| B — Arid | Aswan, Ulaanbaatar |
| C — Temperate | Tunis, Milan |
| D — Continental | Moscow, Yellowknife |
| E — Polar | Longyearbyen, South Pole |

The climate groups are used to organize the comparisons. The two selected locations are examples of their groups, not representatives of every climate in those groups.


### Tools and data sources

- Python and Pandas for processing and analyzing data
- Open-Meteo Historical Weather API for historical weather observations derived from weather models and reanalysis
- Köppen–Geiger climate classification for selecting and organizing locations
- Matplotlib or other visualization tools may be added during the analysis stage

Data sources:

- [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)
- [Köppen–Geiger climate classification](https://koeppen-geiger.vu-wien.ac.at/present.htm)


### Technologies

- Python
- Pandas
- NumPy
- Open-Meteo API
- Matplotlib (planned)
- Streamlit (planned)


### Project Progress

- [x] Initialize GitHub repository
- [x] Establish initial API connection
- [x] Retrieve a small part of the historical weather data and test it
- [x] Retrieve larger historical weather data
- [x] Convert API response into a Pandas DataFrame
- [x] Select cities and long-term analysis period
- [ ] Collect the full dataset
- [ ] Clean and analyze the data
- [ ] Create visualizations
- [ ] Develop Streamlit application



### Current progress

The API connection and data processing have been tested successfully using seven days of weather data for all ten locations.

The test produced a DataFrame containing 70 rows and 11 columns, with no missing values or duplicate city-date combinations.

I then expanded the requested period to 1986–2025. The full request was too large, so I divided the data collection into five-year batches.

The current challenge is handling the API's hourly request limit and making downloads resumable. The complete forty-year dataset has not yet been finalized.

### Next steps

1. Save each successful download batch and skip completed batches when restarting.
2. Collect and combine the complete 1986–2025 dataset.
3. Check data quality and missing observations.
4. Analyze annual temperature trends and apparent temperature differences.
5. Compare the selected locations and create visualizations.

### Project status

**In progress — data collection and validation.**

### How to Run

Install the required packages:

python -m pip install -r requirements.txt

Run the initial API script:

python test_api.py


