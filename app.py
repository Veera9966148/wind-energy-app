import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("wind_energy_rf_model_small.pkl")

st.title("Wind Energy Prediction App")

wind_speed = st.number_input("Wind Speed (m/s)")
wind_direction = st.number_input("Wind Direction (degrees)")
power_lag1 = st.number_input("Previous Power")
wind_lag1 = st.number_input("Previous Wind Speed")
theoretical_power = st.number_input("Theoretical Power")

wind_speed_cubed = wind_speed ** 3
wind_dir_sin = np.sin(np.radians(wind_direction))
wind_dir_cos = np.cos(np.radians(wind_direction))

data = pd.DataFrame([[ 
    wind_speed,
    wind_speed_cubed,
    wind_dir_sin,
    wind_dir_cos,
    power_lag1,
    wind_lag1,
    theoretical_power
]], columns=[
    "Wind Speed (m/s)",
    "Wind_Speed_Cubed",
    "Wind_Dir_sin",
    "Wind_Dir_cos",
    "Power_Lag1",
    "Wind_Lag1",
    "Theoretical_Power_Curve (KWh)"
])

if st.button("Predict"):
    prediction = model.predict(data)
    st.success(f"Predicted Power Output: {prediction[0]:.2f} kW")
