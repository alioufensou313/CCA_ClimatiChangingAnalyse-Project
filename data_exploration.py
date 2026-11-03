
import pandas as pd

# 1. LOAD OUR SAVED DATASET
# Change the filename if your CSV has a different name.

df = pd.read_csv(
    "weather_1986_2025.csv",
    parse_dates=["date"]
)

# 2. UNDERSTAND THE DATASET

print("\nDATASET SHAPE:")
print(df.shape)

print("\nFIRST FIVE ROWS:")
print(df.head())

print("\nCOLUMN INFORMATION:")
df.info()

# 3. DESCRIPTIVE STATISTICS

print("\nGENERAL STATISTICS:")
print(df.describe().round(2))

print("\nAVERAGE TEMPERATURE BY CITY:")
print(
    df.groupby("city")["temperature_mean"]
    .mean()
    .round(2)
)

# 4. DATA QUALITY CHECKS

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE CITY-DATE ROWS:")
print(df.duplicated(subset=["city", "date"]).sum())

# Temperature consistency
invalid_temperatures = (
    (df["temperature_min"] > df["temperature_mean"]) |
    (df["temperature_mean"] > df["temperature_max"])
)

print("\nINVALID TEMPERATURE ROWS:")
print(invalid_temperatures.sum())

# Humidity must be between 0 and 100%
invalid_humidity = (
    (df["relative_humidity"] < 0) |
    (df["relative_humidity"] > 100)
)

print("\nINVALID HUMIDITY ROWS:")
print(invalid_humidity.sum())

# Sunshine hours must be between 0 and 24
invalid_sunshine = (
    (df["sunshine_hours"] < 0) |
    (df["sunshine_hours"] > 24)
)

print("\nINVALID SUNSHINE ROWS:")
print(invalid_sunshine.sum())

# 5. CHECK DATE COVERAGE

print("\nDATE RANGE BY CITY:")
print(
    df.groupby("city")["date"].agg(["min", "max", "count"])
)
