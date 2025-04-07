import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("/home/mac-aphid/Desktop/simulationAssignment/best_crop_yield_model.pkl")

st.set_page_config(page_title="Crop Yield Predictor", layout="wide")
st.title("🌾 Crop Yield Prediction App")

# Add custom CSS for adjusting heights
st.markdown(
    """
    <style>
    .css-1d391kg {  /* Sidebar container class */
        height: 90vh;  /* Set sidebar height to 90% of the viewport height */
    }
    .css-1lcbkh0 {  /* Main content container class */
        height: 90vh;  /* Set main content height to 90% of the viewport height */
    }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown("""
Enter values for environmental and soil conditions to predict expected crop yield.
""")

# Input UI grouped by feature categories
def get_user_input():
    inputs = {}

    st.header("💧 Humidity Features")
    inputs["humidity_feature_40"] = st.slider(f"Humidity Feature (Average)", 20.0, 90.0, 55.0)


    st.header("🌡️ Temperature Features")
    inputs["temp_feature_0"] = st.slider(f"Temperature Feature (Average)", 15.0, 35.0, 25.0)

    st.header("🌧️ Rainfall Features")
    inputs["rain_feature_20"] = st.slider(f"Rainfall Feature (Average)", 100.0, 1200.0, 600.0)

    
    st.header("🌱 Soil Quality Features")
    inputs["soil_feature_60"] = st.slider(f"Soil Feature (Average)", 0.3, 1.0, 0.65)

    st.header("⚙️ Miscellaneous Agro Features")
    inputs["misc_feature_80"] = st.slider(f"Misc Feature (Average)", -3.0, 3.0, 0.0)

    return pd.DataFrame([inputs])

# Capture user input
input_df = get_user_input()

# Predict yield
if st.button("📈 Predict Crop Yield"):
    prediction = model.predict(input_df)[0]
    st.success(f"🌾 Estimated Crop Yield: **{prediction:.2f} units**")
