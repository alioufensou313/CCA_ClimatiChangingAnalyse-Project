
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Weather Report",
    page_icon="🌍",
    layout="wide"
)

# Dashboard title
st.title("🌍 Weather Report")
st.write("Exploring 40 Years of Weather Across Contrasting Environments (1986–2025)")

# Our five climate groups
climate_groups = {
    "A - Tropical": ["Kisangani", "Darwin"],
    "B - Dry": ["Aswan", "Ulaanbaatar"],
    "C - Temperate": ["Tunis", "Milan"],
    "D - Continental": ["Moscow", "Yellowknife"],
    "E - Polar": ["Longyearbyen", "South Pole"]
}

# Climate group selection
selected_group = st.selectbox(
    "Choose a climate group:",
    list(climate_groups.keys())
)

# City selection
selected_city = st.selectbox(
    "Choose a location:",
    climate_groups[selected_group]
)

st.success(f"Selected location: {selected_city}")
