import time
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry


# 1. SET UP THE OPEN-METEO API CLIENT

cache_session = requests_cache.CachedSession(
    ".cache", expire_after=-1
)

retry_session = retry(
    cache_session, retries=5, backoff_factor=0.2
)

openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://archive-api.open-meteo.com/v1/archive"


# 2. DEFINE OUR 10 LOCATIONS AND CLIMATE GROUPS

cities = [
    {"name": "Kisangani", "lat": 0.5153, "lon": 25.191, "group": "A"},
    {"name": "Darwin", "lat": -12.4611, "lon": 130.8418, "group": "A"},

    {"name": "Aswan", "lat": 24.0908, "lon": 32.8994, "group": "B"},
    {"name": "Ulaanbaatar", "lat": 47.9077, "lon": 106.8832, "group": "B"},

    {"name": "Tunis", "lat": 36.819, "lon": 10.1658, "group": "C"},
    {"name": "Milan", "lat": 45.4642, "lon": 9.1900, "group": "C"},

    {"name": "Moscow", "lat": 55.752, "lon": 37.6178, "group": "D"},
    {"name": "Yellowknife", "lat": 62.4541, "lon": -114.3725, "group": "D"},

    {"name": "Longyearbyen", "lat": 78.2233, "lon": 15.6469, "group": "E"},
    {"name": "South Pole", "lat": -90.0, "lon": 0.0, "group": "E"}
]


# 3. DEFINE THE API REQUEST


# 3. DEFINE THE VARIABLES AND TIME PERIODS

daily_variables = [
    "temperature_2m_mean",
    "temperature_2m_max",
    "temperature_2m_min",
    "apparent_temperature_mean",
    "relative_humidity_2m_mean",
    "sunshine_duration"
]

periods = [
    (1986, 1990),
    (1991, 1995),
    (1996, 2000),
    (2001, 2005),
    (2006, 2010),
    (2011, 2015),
    (2016, 2020),
    (2021, 2025)
]


# 4. REQUEST AND PROCESS SMALL BATCHES

all_dataframes = []

for city in cities:

    for start_year, end_year in periods:

        params = {
            "latitude": city["lat"],
            "longitude": city["lon"],
            "start_date": f"{start_year}-01-01",
            "end_date": f"{end_year}-12-31",
            "daily": daily_variables,
            "timezone": "auto"
        }

        print(
            f"Downloading {city['name']}: "
            f"{start_year}-{end_year}",
            flush=True
        )

        responses = openmeteo.weather_api(url, params=params)
        time.sleep(10)
        response = responses[0]
        daily = response.Daily()

        daily_data = {
            "date": pd.date_range(
                start=params["start_date"],
                periods=len(daily.Variables(0).ValuesAsNumpy()),
                freq="D"
            ),
            "temperature_mean": daily.Variables(0).ValuesAsNumpy(),
            "temperature_max": daily.Variables(1).ValuesAsNumpy(),
            "temperature_min": daily.Variables(2).ValuesAsNumpy(),
            "apparent_temperature": daily.Variables(3).ValuesAsNumpy(),
            "relative_humidity": daily.Variables(4).ValuesAsNumpy(),
            "sunshine_duration": daily.Variables(5).ValuesAsNumpy()
        }

        city_dataframe = pd.DataFrame(daily_data)

        city_dataframe["city"] = city["name"]
        city_dataframe["group"] = city["group"]

        all_dataframes.append(city_dataframe)


# 5. COMBINE ALL BATCHES

daily_dataframe = pd.concat(
    all_dataframes, ignore_index=True
)

print("All batches combined!")


# 6. COMBINE ALL LOCATIONS INTO ONE DATAFRAME

daily_dataframe = pd.concat(
    all_dataframes, ignore_index=True
)


# 7. CREATE ADDITIONAL ANALYSIS VARIABLES

# Convert sunshine duration from seconds to hours
daily_dataframe["sunshine_hours"] = (
    daily_dataframe["sunshine_duration"] / 3600
)

# Difference between apparent and actual temperature
daily_dataframe["feels_like_difference"] = (
    daily_dataframe["apparent_temperature"]
    - daily_dataframe["temperature_mean"]
)


# 8. DISPLAY of the DATASET

print("\nFirst five rows:")
print(daily_dataframe.head())

print("\nDataset shape:")
print(daily_dataframe.shape)

print("\nTotal rows:")
print(len(daily_dataframe))

print("\nCities per climate group:")
print(daily_dataframe.groupby("group")["city"].nunique())


# 9. VALIDATE DATA QUALITY

print("\nMissing values:")
print(daily_dataframe.isnull().sum())

print("\nRows per city:")
print(daily_dataframe.groupby(["group", "city"]).size())

print("\nDuplicate city-date rows:")
print(
    daily_dataframe.duplicated(
        subset=["city", "date"]
    ).sum()
)

daily_dataframe.to_csv("weather_1986_2025.csv", index=False)

print("Dataset saved successfully!")