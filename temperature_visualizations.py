
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the annual statistics
df = pd.read_csv("outputs/annual_summary.csv")


# Create a reusable function
def plot_temperature_trend(city):

    # Select the chosen city's data
    city_data = df[df["city"] == city].sort_values("year")

    # Check that the city exists
    if city_data.empty:
        print("City not found:", city)
        return

    # Calculate the linear trend
    slope, intercept = np.polyfit(
        city_data["year"],
        city_data["annual_mean_temperature"],
        1
    )

    trend_line = slope * city_data["year"] + intercept

    # Draw the annual temperature
    plt.figure(figsize=(10, 5))

    plt.plot(
        city_data["year"],
        city_data["annual_mean_temperature"],
        label="Annual temperature"
    )

    # Draw the trend line
    plt.plot(
        city_data["year"],
        trend_line,
        label="Linear trend"
    )

    plt.title(f"{city}: Annual Mean Temperature (1986–2025)")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# Let the user choose a city
print("\nAvailable cities:")
print(", ".join(sorted(df["city"].unique())))

selected_city = input("\nEnter a city name: ").strip()

plot_temperature_trend(selected_city)
