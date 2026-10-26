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

## Weather variables
- Mean temperature (°C)
- Mean apparent temperature (°C)
- Mean relative humidity (%)

## Locations

The initial API request includes three geographical locations:

Milan, Italy

Tunis, Tunisia

A location in France (coordinates: 46°N, 2°E)

Current Testing Period

### The first working dataset covers January 1–7, 2020.

This short period is used to verify that the API connection, data retrieval, and DataFrame construction work correctly before expanding the analysis.
### Planned Analysis

We will calculate the difference between apparent temperature and actual temperature, investigate its relationship with relative humidity, and compare results across seasons, years, and cities.

The historical analysis will help us examine whether these relationships have remained stable or changed over time.

# How to Run

Install the required packages:

python -m pip install -r requirements.txt

Run the initial API script:

python test_api.py

# Project Status

In development — API integration and initial data exploration completed.

This project is developed incrementally, with changes documented through Git and GitHub.

## Selection of Climate Anchor Points

Rather than analyzing a large number of randomly selected cities, this project focuses on eight carefully chosen geographical anchor points. Each location illustrates a distinctive climate environment, allowing us to investigate how temperature, humidity, apparent temperature, and sunshine duration vary across different regions of the world.

### Selected Locations

| City | Country | Climate Profile | Reason for Selection |
|---|---|---|---|
| Singapore | Singapore | Tropical Rainforest | High temperatures and humidity throughout the year, with limited seasonal temperature variation. |
| Aswan | Egypt | Hot Desert | Extremely dry conditions, intense summer heat, and abundant sunshine. |
| Tunis | Tunisia | Mediterranean | Hot, relatively dry summers and mild, wetter winters. |
| London | United Kingdom | Temperate Oceanic | Maritime influence, moderate temperatures, and relatively mild seasonal contrasts. |
| Ulaanbaatar | Mongolia | Cold Semi-Arid | Strong continental temperature variations, with extremely cold winters and relatively warm summers. |
| Tromsø | Norway | Subarctic | High northern latitude, cold conditions, and extreme seasonal daylight variation. |
| Sydney | Australia | Humid Subtropical | Warm summers, mild winters, and opposite seasons compared with Northern Hemisphere cities. |
| Ushuaia | Argentina | Subpolar Oceanic | Cool maritime conditions at a high southern latitude, providing a contrast with northern high-latitude locations. |

### Why Only Eight Cities?

The objective is not to represent every climate or geographical region on Earth, but to study a small number of contrasting environments.

Eight locations provide sufficient climatic diversity while keeping the dataset manageable, the comparisons meaningful, and the visualizations easy to interpret.

The selection also introduces geographical contrasts between the Northern and Southern Hemispheres, allowing us to examine differences in seasonal patterns.

### Selection Methodology

The cities were selected using a **purposive sampling approach**, based on their geographical positions, general climate characteristics, and relevance to the project's research questions.

Each anchor point is treated as a case study of a particular climate environment rather than a statistically representative sample of an entire region.

This approach allows the project to remain focused on its primary objective: **Exploring Forty Years of Weather Across Contrasting Environments.**

### Limitations

The selected cities cannot represent global climate conditions or all locations within their respective climate zones. Local geography, elevation, coastal influences, and urbanization can also affect the observed weather.

Therefore, conclusions will focus on differences and historical trends within the selected locations, rather than making generalizations about the entire planet.