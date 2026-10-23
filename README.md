# Climate Change Analysis Project

## Project Overview
A Data science project designed to analyze a large historical temperature trends since 19-- using the Open-Meteo API and Streamlit.
This project aims to investigate how temperatures have changed over time using historical weather data from the Open-Meteo API and represent it in a creative and comprehensive way to help make conclusions for the specialists or give a global vue to the curious ones 

The main objective is to analyze long-term temperature trends as our professor mentionned (decades), compare different cities, and identify possible signs of climate change.

## Data Source

- **API:** Open-Meteo Historical Weather API
- **Website:** https://open-meteo.com/en/docs/historical-weather-api
- **Data:** Historical daily temperatures
- **Time period:** To be defined (long-term analysis starting from 1940 where data is available)
- **Locations:** To be selected

## Technologies

- Python
- Pandas
- NumPy
- Open-Meteo API
- Matplotlib (planned)
- Streamlit (planned)

## Project Progress

- [x] Initialize GitHub repository
- [x] Establish initial API connection
- [x] Retrieve a small part of the historical weather data and test it
- [ ] Retrieve larger historical weather data
- [ ] Convert API response into a Pandas DataFrame
- [ ] Select cities and long-term analysis period
- [ ] Collect the full dataset
- [ ] Clean and analyze the data
- [ ] Create visualizations
- [ ] Develop Streamlit application

## Installation and Usage

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the initial API test:

```bash
python test_api.py
```

## Project Status

Work in progress — initial test completed moving to collecting larger portion of data.