
import pandas as pd
import matplotlib.pyplot as plt

# Load the temperature trends already calculated
df = pd.read_csv("outputs/temperature_trends.csv")

# Two locations for each Koppen-Geiger climate group
climate_groups = {
    "A": ["Kisangani", "Darwin"],
    "B": ["Aswan", "Ulaanbaatar"],
    "C": ["Tunis", "Milan"],
    "D": ["Moscow", "Yellowknife"],
    "E": ["Longyearbyen", "South Pole"]
}

group_names = {
    "A": "Tropical",
    "B": "Dry",
    "C": "Temperate",
    "D": "Continental",
    "E": "Polar"
}

print("\nAvailable climate groups:")

for group, name in group_names.items():
    print(f"{group} - {name}")

selected_group = input("\nChoose a climate group (A-E): ").strip().upper()

if selected_group not in climate_groups:
    print("Invalid climate group.")

else:
    selected_cities = climate_groups[selected_group]

    # Keep only the two selected locations
    comparison = df[df["city"].isin(selected_cities)]

    if len(comparison) != 2:
        print("Missing data for one or both locations.")

    else:
        # Create the comparison graph
        plt.figure(figsize=(8, 5))

        bars = plt.bar(
            comparison["city"],
            comparison["trend_per_decade"]
        )

        # Display the exact value above each bar
        for bar in bars:
            height = bar.get_height()

            plt.annotate(
                f"{height:+.3f}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5 if height >= 0 else -5),
                textcoords="offset points",
                ha="center",
                va="bottom" if height >= 0 else "top"
            )

        # Graph title and labels
        plt.title(
            f"Group {selected_group} - "
            f"{group_names[selected_group]} Climate\n"
            "Estimated Temperature Trends (1986-2025)"
        )

        plt.xlabel("Location")
        plt.ylabel("Linear temperature trend (°C per decade)")

        # Zero reference line
        plt.axhline(0, color="gray", linestyle="--")

        plt.grid(axis="y", alpha=0.3)
        plt.margins(y=0.15)
        plt.tight_layout()
        plt.show()

        # Print the values in the terminal
        print("\nTemperature trends:")
        print(
            comparison[
                ["city", "trend_per_decade"]
            ].to_string(index=False)
        )
