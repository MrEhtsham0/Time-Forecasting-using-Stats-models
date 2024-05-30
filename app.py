import streamlit as st
import pickle
from datetime import datetime

# Function to load the SARIMA model
@st.cache(allow_output_mutation=True)
def load_model():
    with open("SARIMA.pkl", 'rb') as file:
        model = pickle.load(file)
    return model

# Initialize the Streamlit app
st.title("SARIMA Model Prediction")

# Load the SARIMA model
model = load_model()
st.write("Model loaded successfully.")

# Input start and end dates for prediction
start_date = st.date_input("Start Date", value=datetime(1956, 6, 6), min_value=datetime(1950, 1, 1), max_value=datetime(2025, 12, 31))
end_date = st.date_input("End Date", value=datetime(1960, 12, 1), min_value=start_date, max_value=datetime(2025, 12, 31))

# Predict button
if st.button("Predict"):
    # Convert dates to datetime objects
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.min.time())
    
    # Make predictions
    predictions = model.predict(start=start_datetime, end=end_datetime)
    
    # Display predictions
    st.subheader("Predictions:")
    st.write(predictions)

    # Plot the predictions
    st.subheader("Prediction Plot:")
    st.line_chart(predictions)
