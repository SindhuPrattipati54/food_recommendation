import streamlit as st

def personalized_recommendations_survey():
    st.title("Personalized Recommendations Survey")

    st.write("1. How would you describe your mood today?")
    mood_options = ["Happy", "Lazy", "Bored", "Stressed", "Depressed", "Hungry", "None"]
    mood = st.radio("Select your mood:", mood_options)

    st.write("2. Which cuisines do you want to try today?")
    cuisine_options = ["Italian", "Mexican", "Indian", "Chinese", "Thai", "Mongolian", "American"]
    cuisine = st.radio("Select your cuisine:", cuisine_options)

    st.write("3. Do you have any dietary restrictions or preferences?")
    dietary_preferences = st.checkbox("Vegetarian")
    vegan = st.checkbox("Vegan")
    gluten_free = st.checkbox("Gluten-Free")

    st.write("4. Are there specific beverages you enjoy?")
    coffee = st.checkbox("Coffee")
    tea = st.checkbox("Tea")
    smoothies = st.checkbox("Smoothies")
    cocktails = st.checkbox("Cocktails")

    st.write("5. How do you feel about spice levels in your food?")
    spice_level_options = ["Mild", "Medium", "Spicy"]
    spice_level = st.radio("Select your spice level:", spice_level_options)

    st.write("6. How would you describe your current craving?")
    craving_options = ["Comfort Food", "Light and Refreshing", "Indulgent"]
    craving = st.radio("Select your craving:", craving_options)

    st.write("7. Do you have any food allergies we should be aware of?")
    allergy_information = st.text_area("Enter your allergy information:")

    submit_button = st.button("Submit")

    if submit_button:
        # You can process the survey responses here
        st.success("Survey submitted successfully!")

if __name__ == "__main__":
    personalized_recommendations_survey()
