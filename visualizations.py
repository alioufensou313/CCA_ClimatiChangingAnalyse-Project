import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load our annual statistics
df = pd.read_csv("outputs/annual_summary.csv")

# Select Milan
milan = df[df["city"] == "Milan"]

# Calculate the trend line
slope, intercept = np.polyfit(
    milan["year"],
    milan["annual_mean_temperature"],
    1
)

trend_line = slope * milan["year"] + intercept

# Draw the graph
plt.plot(
    milan["year"],
    milan["annual_mean_temperature"],
    label="Annual temperature"
)

plt.plot(
    milan["year"],
    trend_line,
    label="Linear trend"
)

plt.title("Milan: Annual Mean Temperature (1986–2025)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.show()
