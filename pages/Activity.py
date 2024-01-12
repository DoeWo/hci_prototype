import streamlit as st
from streamlit_folium import folium_static
import folium

# Header
st.title("Your Activity")


# Dropdown for selecting current activity
activity_options = ["Work", "Sport", "Petting Dog", "Relaxing", "Reading", "Cooking"]
selected_activity = st.selectbox("What are you currently doing?", activity_options)

# Input field for heart rate
heart_rate = st.number_input("Enter your heart rate (beats per minute)", min_value=0)


# Function to generate recommendations based on activity and heart rate
def generate_recommendations(activity, hr):
    recommendations = ""
    if hr < 60 or hr > 100:
        recommendations = "Your heart rate is outside the normal resting range. Please consult a doctor if you feel unwell."
    else:
        if activity == "Work":
            recommendations = "Take short breaks and stay hydrated."
        elif activity == "Sport":
            recommendations = "Maintain your pace, and remember to cool down afterwards."
        elif activity == "Petting Dog":
            recommendations = "Relax and enjoy your time with your pet."
        elif activity == "Relaxing":
            recommendations = "Keep staying relaxed and maintain a comfortable posture."
        elif activity == "Reading":
            recommendations = "Ensure good lighting to avoid eye strain."
        elif activity == "Cooking":
            recommendations = "Stay safe and enjoy your cooking session."
    
    return recommendations


# Display recommendations
if heart_rate:
    recommendations = generate_recommendations(selected_activity, heart_rate)
    st.subheader("Recommendations:")
    st.write(recommendations)

# Function to create a Folium map with activity markers
def create_map_with_activities(location, activity):
    m = folium.Map(location=location, zoom_start=12)

    # Mock locations for different activities in Munich
    activity_locations = {
        "Work": [48.137154, 11.576124],  # Near Marienplatz
        "Sport": [48.1735, 11.5461],     # Olympiapark
        "Petting Dog": [48.1642, 11.6060], # Englischer Garten
        "Relaxing": [48.138631, 11.584509], # Hofgarten
        "Reading": [48.1478, 11.5698],     # Munich City Library
        "Cooking": [48.1351, 11.5820]      # Viktualienmarkt (for shopping ingredients)
    }

    # Add a marker for the selected activity
    if activity in activity_locations:
        folium.Marker(activity_locations[activity], tooltip=activity).add_to(m)
    return m

# Streamlit app layout
st.title("Your current position")


# Default location for Munich
location = [48.1351, 11.5820]

# Create and display the map with activity markers
#st.subheader("Folium Map with Activity Markers")
map_here = create_map_with_activities(location, selected_activity)
folium_static(map_here)


# To run the app, save this script as `app.py`, and in the terminal, run `streamlit run app.py`.
