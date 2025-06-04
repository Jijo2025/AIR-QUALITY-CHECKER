import pickle
import streamlit as st

# Load the model
with open(r"C:\Users\gamer\main_project.pkl", 'rb') as file:
    randreg = pickle.load(file)

# Streamlit page config
st.set_page_config(page_title="🌫️ AQI Predictor", layout="centered", page_icon="🌍")

# Custom background & CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f2f6fc;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        text-align: center;
    }
    .footer {
        font-size: 12px;
        text-align: center;
        color: #999;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🌫️ AQI Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check air quality instantly by entering key pollutants</div>',
            unsafe_allow_html=True)

# AQI Info
with st.expander("📘 What is AQI?"):
    st.markdown("""
    The **Air Quality Index (AQI)** is a measure used to report daily air quality.
    It tells you how clean or polluted the air is and what associated health effects might be a concern.

    AQI is based on:
    - **CO**: Carbon Monoxide
    - **O₃**: Ozone
    - **NO₂**: Nitrogen Dioxide
    - **SO₂**: Sulfur Dioxide
    - **PM2.5**: Fine Particles
    - **PM10**: Coarse Particles

    **AQI Categories**:
    - 🟢 0–50: Good
    - 🟡 51–100: Moderate
    - 🟠 101–150: Unhealthy for Sensitive Groups
    - 🔴 151–200: Unhealthy
    - 🟣 201–300: Very Unhealthy
    - ⚫ 301–500: Hazardous
    """)

st.markdown("#### 🔢 Enter Pollutant Concentrations")

# Layout with 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("🚗 CO (mg/m³)", format="%.2f", min_value=0.0)
    d = st.number_input("🔥 SO₂ (μg/m³)", format="%.2f", min_value=0.0)

with col2:
    b = st.number_input("🌞 O₃ (μg/m³)", format="%.2f", min_value=0.0)
    e = st.number_input("🌪️ PM2.5 (μg/m³)", format="%.2f", min_value=0.0)

with col3:
    c = st.number_input("🏭 NO₂ (μg/m³)", format="%.2f", min_value=0.0)
    f = st.number_input("🌫️ PM10 (μg/m³)", format="%.2f", min_value=0.0)

st.markdown("---")

# Predict button
if st.button("🚀 Predict AQI"):
    v = randreg.predict([[a, b, c, d, e, f]])
    aqi = v[0]

    if aqi <= 50:
        status = "🟢 Good"
    elif aqi <= 100:
        status = "🟡 Moderate"
    elif aqi <= 150:
        status = "🟠 Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        status = "🔴 Unhealthy"
    elif aqi <= 300:
        status = "🟣 Very Unhealthy"
    else:
        status = "⚫ Hazardous"

    st.markdown(f"""<div style='background-color:#dff0d8;padding:20px;border-radius:10px;'>
        <h3 style='color:#2e7d32;'>✅ Predicted AQI: {aqi:.2f}</h3>
        <h4 style='color:#0074cc;'>🌐 Air Quality Level: {status}</h4>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ by Alen | Powered by Machine Learning</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
