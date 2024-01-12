import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np    

# Function to create a sample pie chart for macronutrients
def create_pie_chart(data):
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title("Macronutrient Breakdown")
    return plt

# Mock data for each day (replace with real data)
weekly_intake = {
    "Monday": {"Carbohydrates": 50, "Protein": 20, "Fats": 30},
    "Tuesday": {"Carbohydrates": 60, "Protein": 25, "Fats": 15},
    "Wednesday": {"Carbohydrates": 55, "Protein": 20, "Fats": 25},
    "Thursday": {"Carbohydrates": 40, "Protein": 30, "Fats": 30},
    "Friday": {"Carbohydrates": 45, "Protein": 25, "Fats": 30},
    "Saturday": {"Carbohydrates": 50, "Protein": 20, "Fats": 30},
    "Sunday": {"Carbohydrates": 60, "Protein": 15, "Fats": 25}
}

# Sidebar controls (you can add more controls if needed)
st.sidebar.subheader("Nutrition Settings")
# Example: Select a day to view nutrition data
selected_day = st.sidebar.selectbox("Select Day", list(weekly_intake.keys()))

# Displaying the pie chart for macronutrient breakdown
st.subheader(f"Nutritional Breakdown for {selected_day}")
daily_data = pd.Series(weekly_intake[selected_day], name="Percentage")
st.pyplot(create_pie_chart(daily_data))

# Displaying recommendations based on the breakdown
st.subheader("Daily Recommendations")

# Example conditional logic for recommendations
if daily_data["Carbohydrates"] > 55:
    st.markdown("* Consider reducing carbohydrate intake and increasing protein and fiber.")
elif daily_data["Protein"] < 20:
    st.markdown("* Look to incorporate more protein-rich foods like lean meats, beans, or tofu.")
elif daily_data["Fats"] > 30:
    st.markdown("* Your fat intake is on the higher side. Balance it with unsaturated fats and reduce saturated fats.")

# Additional recommendations or information
# ...

# To run the app, save this script as `app.py`, and in the terminal, run `streamlit run app.py`.
