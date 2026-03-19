import json
import streamlit as st

# Load conversion factors from JSON
@st.cache_data
def load_factors():
    with open("Conversions/Factor_Table.json", "r") as f:
        return json.load(f)

data = load_factors()

st.title("Emissions Conversion Calculator")
st.write("Calculate CO₂ emissions from electricity or gas usage using the JSON factor table.")

# --- User Inputs ---
emission_type = st.selectbox(
    "Select emission type",
    options=list(data.keys()),
    format_func=lambda x: x.capitalize()
)

year = st.selectbox(
    "Select year",
    options=list(data[emission_type].keys())
)

factor = data[emission_type][year]

if factor is None:
    st.warning("⚠️ The conversion factor for this year is not populated.")
else:
    kwh = st.number_input(
        "Enter energy consumption (kWh)",
        min_value=0.0,
        step=0.1
    )

    if st.button("Calculate CO₂ Emissions"):
        co2 = kwh * factor

        st.success(f"### Result\n**{kwh} kWh** of **{emission_type.capitalize()}** in **{year}** emits: {co2:.2f} tonnes CO₂")

st.header("Gigajoules to kWh Converter")

gj_value = st.number_input(
    "Enter energy in gigajoules (GJ)",
    min_value=0.0,
    step=0.1
)

if st.button("Convert to kWh"):
    kwh_result = gj_value * 277.78
    st.success(f"{gj_value} GJ = {kwh_result:.2f} kWh")