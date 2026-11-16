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
- [x] Collect the full dataset
- [x] Clean and analyze the data
- [%] Create visualizations
- [ ] Develop Streamlit application



### Current progress

The API connection and data processing have been tested successfully using seven days of weather data for all ten locations.

The test produced a DataFrame containing 70 rows and 11 columns, with no missing values or duplicate city-date combinations.

I then expanded the requested period to 1986–2025. The full request was too large, so I divided the data collection into five-year batches.

The current challenge is handling the API's hourly request limit and making downloads resumable. The complete forty-year dataset has not yet been finalized.

4.Current progress __ November 2026
The data collection stage is now complete!
After successfully testing the API with seven days of data for ten locations, I expanded the period to 1986–2025. My first attempt failed because the API couldn't handle the whole request at once.
I solved this by dividing the data into five-year periods for each location, giving me 80 smaller requests. I also encountered minute and hourly API limits, so I added delays between requests.
After several attempts, I managed to download and combine the complete dataset.

5.Current progress __ November 2026


***Final dataset***

10 locations across the five major Köppen–Geiger climate groups

40 years of daily weather data (1986–2025)

146,100 observations and 11 columns

6 weather variables and 2 calculated variables

No missing values or duplicate city-date combinations in the initial checks

The dataset is saved locally as a CSV file.

### Next steps

1. Save each successful download batch and skip completed batches when restarting.
2. Collect and combine the complete 1986–2025 dataset.
3. Check data quality and missing observations.
4. Analyze annual temperature trends and apparent temperature differences.
5. Compare the selected locations and create visualizations.

Current stage: Data exploration and validation

Now that the data has been collected, I'm moving on to understanding it before creating graphs.

I plan to check whether the temperature, humidity and sunshine measurements are reasonable, examine the distributions, and identify unusual values that might need further investigation.

After that, I'll calculate annual and seasonal statistics and start comparing temperature trends across locations.


# Data Exploration and Quality Checks

A separate Python script, data_exploration.py, was created to load and analyse the saved CSV dataset using Pandas.

The first stage included:

Checking the dataset dimensions and data types.

Displaying the first records and descriptive statistics.

Checking missing values and duplicate city-date records.

Checking the consistency of minimum, mean and maximum temperatures.

Checking humidity and sunshine-hour values.

Verifying date coverage for every location.

The initial checks found no missing values, duplicate city-date records or invalid values in the checks performed.

Data Preparation and Additional Variables

Two additional variables were created:

sunshine_hours: sunshine duration converted from seconds into hours.

feels_like_difference: apparent temperature minus mean air temperature.

The year was also extracted from each date to support annual analysis.

Statistical Analysis

#### City-Level Statistics

Daily records were grouped by climate group and city to calculate average temperature, maximum and minimum daily temperature averages, apparent temperature, relative humidity, sunshine hours and temperature standard deviation.

#### Annual Statistics

Daily records were grouped by city and year to calculate annual averages.

This produced 400 annual records (10 locations × 40 years).

Annual Temperature Trends

Linear regression was used to estimate:

Temperature trend per decade.

Estimated temperature change between 1986 and 2025.

R-squared, indicating how well the fitted linear trend represents the annual temperature data.

Annual Temperature Anomalies

The period 1986–2005 was selected as the reference period.

For each city, its average annual temperature over this baseline period was calculated. The annual temperature anomaly was then calculated for every year from 1986 to 2025 by subtracting the city's baseline average from that year's average temperature.

#### Current Progress

Historical data collection completed.

Dataset loaded and explored using Pandas.

Initial data quality checks completed.

City-level and annual statistics calculated.

Linear temperature trends estimated.

Annual temperature anomalies calculated.

## First Visualization

I started the visualization stage using Matplotlib.

For my first test, I selected Milan and created a graph showing its annual mean temperature between 1986 and 2025.

The graph contains two lines:
- The annual mean temperature, showing how temperatures changed from one year to another.
- A linear trend line, showing the general temperature tendency over the 40-year period.

The graph uses the annual statistics that I previously calculated with Pandas. This means I can create visualizations without downloading the historical data again.

My next step is to make the visualization work for all ten locations.

## Temperature Trend Visualizations

I first created a graph showing Milan's annual mean temperature from 1986 to 2025 using Matplotlib.

After testing it, I created a new script called `temperature_visualizations.py` to make the visualization reusable for all ten locations.

The script asks the user to enter a city name and then displays its annual mean temperature together with a linear trend line.

I used a Python function to avoid repeating the same plotting code for each city.

The script reads the annual statistics saved during data exploration, so I don't need to download the historical data again.

To run the visualization:

```bash
python temperature_visualizations.py

## Temperature Anomaly Visualizations

After creating the annual temperature trend graphs, I continued with temperature anomalies to better understand how temperatures have changed over time.

I created `anomaly_visualizations.py`, which uses the annual temperature anomalies previously calculated in `DataExploration.py`.

The anomalies are calculated relative to the **1986–2005 baseline period**. A positive anomaly means that the year was warmer than the reference average, while a negative anomaly means it was colder.

I also introduced the five Köppen–Geiger climate groups to organize the ten selected locations:

| Group | Climate | Locations |
|---|---|---|
| A | Tropical | Kisangani, Darwin |
| B | Dry | Aswan, Ulaanbaatar |
| C | Temperate | Tunis, Milan |
| D | Continental | Moscow, Yellowknife |
| E | Polar | Longyearbyen, South Pole |

The script first asks the user to select a climate group and then displays its two locations. After choosing a location, it generates an annual temperature anomaly graph with a horizontal zero line representing the baseline average.

I tested the visualization using Milan and Longyearbyen, and both graphs worked successfully.

To run the script:

`python anomaly_visualizations.py`


## Climate Group Temperature Comparisons

After creating the temperature trend and anomaly visualizations, I wanted to compare the two locations selected within each Köppen–Geiger climate group.

I created a new script called `climate_comparison.py`. It reads the temperature trends previously calculated in `DataExploration.py` from `outputs/temperature_trends.csv`.

The script allows the user to select one of the five climate groups (A–E) and displays a bar chart comparing the estimated temperature trend of its two locations.

The warming rates are expressed in **°C per decade** and calculated using linear regression on annual mean temperatures from 1986 to 2025.

For example, in Group D (Continental):
- Moscow: approximately +0.589°C per decade.
- Yellowknife: approximately +0.306°C per decade.

Although both locations belong to the same broad climate group, their estimated warming rates are different.

The graph includes exact values above the bars, a zero reference line, and the study period.

To run the comparison:

`python climate_comparison.py`



### Project status

**In progress — Second visualisation.**

### How to Run

Install the required packages:

python -m pip install -r requirements.txt

Run the initial API script:

python test_api.py


