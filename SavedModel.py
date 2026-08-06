import streamlit as st
import pickle
import os
import time

@st.cache_resource
def load_model():
    if not os.path.exists("house_price_model.pkl"):
        raise FileNotFoundError("The model file 'house_price_model.pkl' does not exist.")

    with open("house_price_model.pkl", "rb") as file:
        model = pickle.load(file)

    return model

if "prediction_count" not in st.session_state:
    st.session_state.prediction_count = 0
st.title("House Price Prediction App")

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

area = st.number_input("Area (in square feet)", min_value=100, max_value=10000, value=1000)
bedrooms = st.slider("Bedrooms", min_value=1, max_value=10, value=3)
age = st.number_input("Age of the house (in years)", min_value=0, max_value=30, value=5)


if st.button("Predict Price"):
    try:
        prediction = model.predict([[area, bedrooms, age]])
        price = prediction[0]

        if price >= 10000000:
         st.success(f"🏡 Predicted House Price: ₹{price/10000000:.2f} Crore")
        else:
         st.success(f"🏡 Predicted House Price: ₹{price/100000:.2f} Lakh")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.exception(e)

st.info(f"Prediction Count: {st.session_state.prediction_count}")

if st.button("Reset Prediction Count"):
    st.session_state.prediction_count = 0
    st.success("Prediction count has been reset.")