import streamlit as st
import joblib

st.title("🔮 Prediction")

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

st.title('Car Purchace Prediction')

scaler=joblib.load(r'models\scaler.joblib')
model=joblib.load(r'models\knn.joblib')

age=st.number_input("Enter your age",
                      min_value=18, max_value=80)
income=st.number_input("Enter your annual income",
                      min_value=10000, max_value=100000000000)

if st.button("Predict"):
    new=[[age,income]]
    scaled=scaler.transform(new)
    st.write("Purchace prediction:", model.predict(scaled)[0])
    if model.predict(scaled)[0]==1:
        st.write("The Customer will Purchace the car")
    else:
        st.write("The Customer will not Purchace the car")