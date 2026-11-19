# Climate Change Analysis Project

## Exploring Forty Years of Weather Across Contrasting Environments

### 1. Project Overview

This is my Python project for exploring how weather conditions have changed in different parts of the world between **1986 and 2025**.

I started by testing the Open-Meteo Historical Weather API with three locations. However, I realized that choosing random cities would not make the comparisons very meaningful.

After exploring different approaches, I decided to use the **Köppen–Geiger climate classification**. I selected two locations from each of the five major climate groups, making ten locations in total.

My main objective is to study long-term temperature trends, temperature anomalies, and differences between locations belonging to the same climate group.

I also included a small additional analysis of humidity and apparent temperature.

### 2. Selected Locations

| Climate Group | Climate Type | Locations |
|---|---|---|
| A | Tropical | Kisangani, Darwin |
| B | Dry | Aswan, Ulaanbaatar |
| C | Temperate | Tunis, Milan |
| D | Continental | Moscow, Yellowknife |
| E | Polar | Longyearbyen, South Pole |

I tried to select locations with different geographical and climate characteristics, even within the same group.

The idea is to investigate whether two locations sharing a broad climate classification also show similar temperature changes.

These locations are examples for comparison and do not represent every region belonging to their climate group.

### 3. Tools and Data Sources

I used the following tools during the project:

- **Python:** Data collection and analysis.
- **Open-Meteo API:** Historical weather data.
- **Pandas:** Data cleaning, grouping and calculations.
- **NumPy:** Linear regression and numerical calculations.
- **Matplotlib:** Creating graphs and visualizations.
- **Google Colab / Jupyter Notebook:** Organizing the final analysis, graphs and interpretations.
- **Git and GitHub:** Saving and tracking project development.

Data sources:

- [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)
- [Köppen–Geiger Climate Classification](https://koeppen-geiger.vu-wien.ac.at/present.htm)

The historical weather data comes from Open-Meteo's historical datasets, which use weather models and reanalysis data.

---

## 4. Data Collection

### First API Tests

I started by learning how to connect Python to the Open-Meteo API.

My first tests used a small number of locations and only a few days of weather data. This helped me understand the API response and how to convert the results into a Pandas DataFrame.

After choosing the ten final locations, I tested the collection process again using seven days of data.

The test produced **70 rows and 11 columns**, with no missing values or duplicate city-date combinations.

### Collecting Forty Years of Data

After the initial tests, I expanded the study period to **1986–2025**.

At first, I tried requesting the entire period directly, but the request was too large.

To solve this problem, I divided the forty years into **eight periods of five years** for each location.

With ten locations, this resulted in 80 smaller requests.

I also encountered API rate limits, so I introduced delays between requests to make the downloading process more stable.

After several attempts, I successfully collected and combined the historical data.

### Final Dataset

The complete dataset contains:

- 10 locations across five climate groups.
- 40 years of daily weather data (1986–2025).
- **146,100 daily observations and 11 columns.**
- Weather measurements including temperature, apparent temperature, humidity and sunshine duration.

The downloaded data was saved locally as `weather_1986_2025.csv`.

This step was particularly important because I learned how to handle larger API requests instead of working only with small test datasets.

---

## 5. Data Exploration and Preparation

After completing the data collection, I created `DataExploration.py` to examine the dataset before building the graphs.

### Data Quality Checks

I checked:

- Dataset dimensions and data types.
- Missing values and duplicate city-date records.
- Minimum, mean and maximum temperature consistency.
- Humidity and sunshine values.
- Date coverage for every location.

The checks did not identify missing values, duplicates or invalid values among the conditions tested.

### Additional Variables

I prepared additional variables for the analysis, including:

- `sunshine_hours`: Sunshine duration converted from seconds into hours.
- `feels_like_difference`: Apparent temperature minus measured air temperature.
- `year`: Extracted from the date to support annual calculations.

### Statistical Analysis

I calculated two main types of statistics.

**City-level statistics:** General averages and descriptive statistics for each location, including temperature, humidity and sunshine.

**Annual statistics:** Average values for each location and year.

The annual aggregation produced **400 records (10 locations × 40 years)**.

I also calculated linear temperature trends, expressed in °C per decade, to estimate how temperatures changed over the study period.

For temperature anomalies, I selected **1986–2005 as the reference period** and compared each year's annual mean temperature with its location's reference average.

The processed results were saved as CSV files for the visualization stage.

---

## 6. Data Visualization and Analysis

After preparing the dataset, I started creating graphs using Matplotlib.

### Annual Temperature Trends

My first visualization was a graph showing Milan's annual mean temperature between 1986 and 2025.

It contained two lines: one showing the annual temperature variations and another showing the estimated linear trend.

After testing this first graph, I extended the visualization to all ten locations.

I also organized the graphs by climate group to make the comparisons easier.

### Temperature Anomalies

Next, I created graphs showing annual temperature anomalies relative to the 1986–2005 reference period.

These graphs help me understand which years were warmer or colder than the historical average for each location.

Using anomalies also makes it easier to compare temperature changes between locations with very different climates.

### Climate Group Comparisons

I compared the estimated warming rates of the two locations belonging to each climate group.

For example, Milan shows a higher warming rate than Tunis, while Longyearbyen has a much stronger estimated trend than the South Pole.

These comparisons helped me understand that locations within the same broad climate group do not necessarily experience similar temperature changes.

### Humidity and Apparent Temperature

As an additional analysis, I explored the relationship between average relative humidity and the difference between apparent and measured air temperature.

The results showed important differences between locations.

I kept this part exploratory because apparent temperature also depends on other environmental factors, including wind and air temperature.

A more detailed study of these relationships could be interesting for future work.

---

## 7. Final Presentation — Jupyter Notebook

During development, I experimented with separate Python visualization scripts and tested a basic Streamlit interface.

However, I eventually decided to use **Jupyter Notebook** for the final version.

Since the main objective of my project is historical weather analysis rather than web application development, I found Jupyter more suitable.

It allows me to present the Python code, graphs and interpretations together and explain the work step by step.

I used Google Colab to develop and execute the notebook.

The final notebook is:

**`CC_Weather_Analysis.ipynb`**

It contains the main temperature analyses, climate group comparisons, humidity analysis, interpretations and conclusions.

The earlier visualization scripts and Streamlit prototype were useful during development, but the notebook became the final presentation format.

---

## 8. Final Project Structure

| File / Folder | Purpose |
|---|---|
| `test_api.py` | Collects historical weather data from Open-Meteo |
| `DataExploration.py` | Checks, processes and analyzes the dataset |
| `CC_Weather_Analysis.ipynb` | Final notebook containing graphs, analysis and conclusions |
| `data/` | Processed CSV files needed to execute the notebook |
| `README.md` | Project explanation and instructions |
| `advancement report.txt` | Record of project development |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from GitHub |

The `data/` folder contains:

- `annual_summary.csv`
- `temperature_trends.csv`
- `annual_temperature_anomalies.csv`

The original daily dataset and intermediate generated files are kept locally.

---

## 9. How to Run the Project

### View the Analysis

Open `CC_Weather_Analysis.ipynb` on GitHub to read the notebook and see its saved graphs and explanations.

### Execute the Notebook

The notebook requires Python, Pandas, NumPy and Matplotlib.

To run it in Google Colab:

1. Open the notebook in Google Colab.
2. Upload the three CSV files from the repository's `data/` folder into a folder named `data` in the Colab session.
3. Run the notebook cells in order.

The notebook uses the processed CSV files, so there is no need to download the forty years of weather data again.

### Run the Original Data Collection and Exploration

The original data collection and processing scripts are included to document how the dataset was prepared.

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

The data collection script is:

```bash
python test_api.py
```

The exploration script is:

```bash
python DataExploration.py
```

These scripts belong to the earlier data collection and preparation stages. The final notebook can be explored independently using the processed CSV files.

---

## 10. Main Findings and Limitations

The analysis shows positive estimated linear temperature trends across all ten selected locations, although the warming rates are different.

Longyearbyen shows the strongest estimated warming trend, while Darwin has the weakest.

The comparisons also show that locations belonging to the same broad climate group can have noticeably different temperature patterns.

However, the results have some limitations.

The ten locations are case studies and cannot represent entire climate groups. Linear regression simplifies long-term temperature changes, and the estimated trends were not tested for statistical significance.

The humidity analysis is also exploratory and does not establish a direct causal relationship between humidity and apparent temperature.

Despite these limitations, this project helped me understand how to collect historical weather data, prepare it with Python and use visualizations to investigate long-term changes.

---

## 11. Project Progress

- [x] Initialize GitHub repository.
- [x] Test the Open-Meteo API.
- [x] Select locations using Köppen–Geiger climate groups.
- [x] Collect the 1986–2025 historical dataset.
- [x] Validate and explore the data.
- [x] Calculate annual statistics, trends and anomalies.
- [x] Create temperature visualizations.
- [x] Compare locations across climate groups.
- [x] Explore humidity and apparent temperature.
- [x] Organize the final analysis in Jupyter Notebook.
- [x] Write interpretations and conclusions.