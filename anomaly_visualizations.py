
import pandas as pd
import matplotlib.pyplot as plt

# Load the annual temperature anomalies
df = pd.read_csv("outputs/annual_temperature_anomalies.csv")

# Our five climate groups
groups = {
    "A": "Tropical",
    "B": "Dry",
    "C": "Temperate",
    "D": "Continental",
    "E": "Polar"
}

# Show available climate groups
print("\nAvailable climate groups:")

for group, name in groups.items():
    print(group, "-", name)

# Ask the user to choose a group
selected_group = input("\nChoose a group (A-E): ").strip().upper()

if selected_group not in groups:
    print("Invalid climate group.")

else:
    # Keep only locations from the selected group
    group_data = df[df["group"] == selected_group]

    # Display the two locations
    cities = sorted(group_data["city"].unique())

    print("\nAvailable locations:")
    for city in cities:
        print("-", city)

    # Ask the user to choose a location
    selected_city = input("\nChoose a city: ").strip()

    city_data = group_data[
        group_data["city"].str.lower() == selected_city.lower()
    ].sort_values("year")

    if city_data.empty:
        print("City not found in this group.")

    else:
        # Draw annual temperature anomalies
        plt.figure(figsize=(10, 5))

        plt.plot(
            city_data["year"],
            city_data["temperature_anomaly"],
            marker="o",
            markersize=3,
            label="Annual anomaly"
        )

        # Zero means equal to the baseline temperature
        plt.axhline(0, color="gray", linestyle="--",
                    label="Baseline (1986-2005)")

        plt.title(
            f"{city_data['city'].iloc[0]} - Annual Temperature Anomalies"
        )

        plt.xlabel("Year")
        plt.ylabel("Temperature anomaly (°C)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

