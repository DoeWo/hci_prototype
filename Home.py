import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to create a sample chart
def create_chart(data_size):
    data = pd.DataFrame(np.random.randn(data_size, 3), columns=['a', 'b', 'c'])
    plt.figure(figsize=(10, 4))
    plt.plot(data)
    plt.legend(data.columns)
    return plt

# Set up the main structure of the app
st.title("Your well-being:")

# Personalize Your Recommendations
st.header("Personalize Your Recommendations")
age = st.slider("Select your age", 18, 100)
activity_level = st.selectbox("Select your activity level", ["Low", "Moderate", "High"])

# Dropdown for well-being goals
well_being_goals = ["Improve Mental Health", "Enhance Physical Fitness", "Reduce Stress", "Improve Sleep Quality"]
selected_goal = st.selectbox("Select your well-being goal", well_being_goals)

# Display user input
st.write("Your Age:", age)
st.write("Your Activity Level:", activity_level)
st.write("Your Well-being Goal:", selected_goal)

if selected_goal == "Improve Mental Health":
    st.image(r"picture\mental_health.jpg", caption="If you want to see the stars, you must be willing to travel through the dark.")
elif selected_goal == "Enhance Physical Fitness":
    st.image(r"picture\physicall_fitnes.jpg", caption="Be stronger than your excuses.")
elif selected_goal == "Reduce Stress":
    st.image(r"picture\reduce_stress.jpg", caption="One of the best ways to reduce stress is to accept the things that you cannot control.")
elif selected_goal == "Improve Sleep Quality":
    st.image(r"picture\sleeping_quality.jpg", caption="Sleep is the best meditation.")
else:
    st.image(r"picture\3dd4a40c-6099-4bf1-a5c6-2740641b5a37.jpg", caption="Peace begins from within, if you are not peaceful inside, the world you see will be chaotic.")


# Displaying charts
col1, col2 = st.columns(2)
with col1:
    st.subheader("Mental Health Trend")
    st.pyplot(create_chart(age))  # Example of using user input in a function
with col2:
    st.subheader("Physical Health Trend")
    st.pyplot(create_chart(age))  # Same as above

st.header("Recommendations for Well-being")
st.write("Based on your input, here are some personalized recommendations:")

# Tailored recommendations based on the selected goal
if selected_goal == "Improve Mental Health":
    st.markdown("* Engage in activities like yoga and meditation")
    st.markdown("* Spend time in nature")
    st.markdown("* Practice mindfulness")

elif selected_goal == "Enhance Physical Fitness":
    st.markdown("* Incorporate regular strength and cardio exercises")
    st.markdown("* Stay consistent with your workout routine")
    st.markdown("* Balance your diet")

elif selected_goal == "Reduce Stress":
    st.markdown("* Practice deep breathing and relaxation techniques")
    st.markdown("* Maintain a healthy work-life balance")
    st.markdown("* Engage in hobbies and activities you enjoy")

elif selected_goal == "Improve Sleep Quality":
    st.markdown("* Establish a regular sleep schedule")
    st.markdown("* Create a comfortable sleep environment")
    st.markdown("* Avoid caffeine and electronics before bedtime")