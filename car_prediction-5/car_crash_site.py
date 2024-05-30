import streamlit as st
import pickle

# Load the pickled model and encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('injury_type_encoder.pkl', 'rb') as f:
    injury_type_encoder = pickle.load(f)
with open('collision_type_encoder.pkl', 'rb') as f:
    collision_type_encoder = pickle.load(f)
with open('primary_factor_encoder.pkl', 'rb') as f:
    primary_factor_encoder = pickle.load(f)

# Site Config
st.set_page_config(page_title='Car Crash', page_icon=":oncoming_automobile:", layout="wide")

# --- Header Section ---
with st.container():
    st.subheader("CSC 245 Final Project")
    st.header("Welcome to car crash predictor!")
    st.write("This project aims to predict the severity of a car crash based on various factors.")

# --- Inputs ---
with st.container():
    # Date
    year = st.number_input('Year', min_value=2003, max_value=2024, value=2024)
    month = st.number_input('Month', min_value=1, max_value=12, value=1)
    day = st.number_input('Day', min_value=1, max_value=31, value=1)
    hour = st.number_input('Hour', min_value=0, max_value=23, value=0)

    # Collision Factors
    # Collect the categorical inputs and encode them
    collision_type = st.selectbox('Collision Type', collision_type_encoder.classes_)
    primary_factor = st.selectbox('Primary Factor', primary_factor_encoder.classes_)

    # Encode the categorical inputs
    encoded_collision_type = collision_type_encoder.transform([collision_type])[0]
    encoded_primary_factor = primary_factor_encoder.transform([primary_factor])[0]

    # Is Weekend?
    weekend = st.checkbox('Weekend', value=False)
    weekend_value = 1 if weekend else 0

# --- Predict ---
with st.container():
    if st.button('Predict', key='predict'):
        features = [[year, month, day, hour, encoded_collision_type, encoded_primary_factor, weekend]]
        prediction = model.predict(features)
        # Decode the prediction to its original injury type
        prediction = injury_type_encoder.inverse_transform(prediction)[0]
        st.success('The predicted outcome of this car crash is: {}'.format(prediction))

# --- Possible Injuries ---
with st.container():
    # Display all possible injury types
    st.subheader("Possible Injury Types")
    st.write(injury_type_encoder.classes_)
