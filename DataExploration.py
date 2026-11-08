
import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD THE DATASET
# ==========================================

df = pd.read_csv(
    "weather_1986_2025.csv",
    parse_dates=["date"]
)

print("DATASET LOADED SUCCESSFULLY")
print("Shape:", df.shape)


# ==========================================
# 2. DATA STRUCTURE
# ==========================================

print("\n--- DATA INFORMATION ---")
df.info()

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe().round(2))


# ==========================================
# 3. DATA QUALITY CHECKS
# ==========================================

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\nDuplicate city-date records:")
print(df.duplicated(subset=["city", "date"]).sum())

# Check temperature consistency
invalid_temp = (
    (df["temperature_min"] > df["temperature_mean"]) |
    (df["temperature_mean"] > df["temperature_max"])
)

print("\nInvalid temperature records:", invalid_temp.sum())

# Check humidity
invalid_humidity = (
    (df["relative_humidity"] < 0) |
    (df["relative_humidity"] > 100)
)

print("Invalid humidity records:", invalid_humidity.sum())

# Check sunshine duration
invalid_sunshine = (
    (df["sunshine_hours"] < 0) |
    (df["sunshine_hours"] > 24)
)

print("Invalid sunshine records:", invalid_sunshine.sum())


# ==========================================
# 4. CHECK DATE COVERAGE
# ==========================================

print("\n--- DATE COVERAGE BY CITY ---")

date_coverage = df.groupby("city")["date"].agg(
    ["min", "max", "count", "nunique"]
)

print(date_coverage)


# ==========================================
# 5. STATISTICS BY CITY
# ==========================================

print("\n--- AVERAGE TEMPERATURE BY CITY ---")

city_summary = (
    df.groupby(["group", "city"])
    .agg(
        mean_temperature=("temperature_mean", "mean"),
        mean_max_temperature=("temperature_max", "mean"),
        mean_min_temperature=("temperature_min", "mean"),
        mean_apparent_temperature=("apparent_temperature", "mean"),
        mean_humidity=("relative_humidity", "mean"),
        mean_sunshine_hours=("sunshine_hours", "mean"),
        temperature_std=("temperature_mean", "std")
    )
    .round(2)
)

print(city_summary)


# ==========================================
# 6. ANNUAL TEMPERATURE ANALYSIS
# ==========================================

df["year"] = df["date"].dt.year

annual_summary = (
    df.groupby(["group", "city", "year"])
    .agg(
        annual_mean_temperature=("temperature_mean", "mean"),
        mean_daily_max_temperature=("temperature_max", "mean"),
        mean_daily_min_temperature=("temperature_min", "mean"),
        annual_apparent_temperature=("apparent_temperature", "mean"),
        annual_humidity=("relative_humidity", "mean"),
        annual_sunshine_hours=("sunshine_hours", "mean")
    )
    .reset_index()
    .round(2)
)

# TEMPERATURE TREND BY CITY

import numpy as np

trend_results = []

for city, city_data in annual_summary.groupby("city"):

    slope, intercept = np.polyfit(
        city_data["year"],
        city_data["annual_mean_temperature"],
        1
    )

    trend_per_decade = slope * 10

    trend_results.append({
        "city": city,
        "trend_per_decade": trend_per_decade
    })

trend_df = pd.DataFrame(trend_results)

print("\n--- TEMPERATURE TREND BY CITY ---")
print(trend_df.round(3))

print("\n--- ANNUAL TEMPERATURE SUMMARY ---")
print(annual_summary.head(10))

print("\nAnnual dataset shape:", annual_summary.shape)



# ==========================================
# 7. ANNUAL TEMPERATURE TREND ANALYSIS
# ==========================================

trend_results = []

for city, city_data in annual_summary.groupby("city"):

    # Calculate the linear regression
    slope, intercept = np.polyfit(
        city_data["year"],
        city_data["annual_mean_temperature"],
        1
    )

    # Calculate predicted temperatures
    predicted = slope * city_data["year"] + intercept

    # Calculate R-squared
    actual = city_data["annual_mean_temperature"]
    ss_res = ((actual - predicted) ** 2).sum()
    ss_tot = ((actual - actual.mean()) ** 2).sum()
    r_squared = 1 - (ss_res / ss_tot)

    # Calculate temperature change
    trend_per_decade = slope * 10
    total_change = slope * 39

    trend_results.append({
        "city": city,
        "trend_per_decade": trend_per_decade,
        "estimated_change_1986_2025": total_change,
        "r_squared": r_squared
    })

trend_df = pd.DataFrame(trend_results)

trend_df = trend_df.sort_values(
    "trend_per_decade",
    ascending=False
)

print("\n--- ANNUAL TEMPERATURE TRENDS ---")
print(trend_df.round(3).to_string(index=False))

trend_df.to_csv(
    "outputs/temperature_trends.csv",
    index=False
)


# ==========================================
# 8. ANNUAL TEMPERATURE ANOMALIES
# ==========================================

# Calculate each city's average temperature during 1986-2005
baseline = (
    annual_summary[
        annual_summary["year"].between(1986, 2005)
    ]
    .groupby("city")["annual_mean_temperature"]
    .mean()
    .rename("baseline_temperature")
)

# Attach each city's baseline to its annual records
annual_summary = annual_summary.merge(
    baseline,
    on="city"
)

# Calculate the temperature anomaly
annual_summary["temperature_anomaly"] = (
    annual_summary["annual_mean_temperature"]
    - annual_summary["baseline_temperature"]
)

print("\n--- TEMPERATURE ANOMALIES ---")

print(
    annual_summary[
        ["city", "year", "annual_mean_temperature",
         "baseline_temperature", "temperature_anomaly"]
    ].head(10).round(2)
)

# Save results
annual_summary.to_csv(
    "outputs/annual_temperature_anomalies.csv",
    index=False
)

print("\nTrend and anomaly results saved successfully!")
