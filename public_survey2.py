import streamlit as st

@st.cache
def get_food_items():
    return [
        'chicken minced salad', 'japanese curry arancini with barley salsa',  # ... (your complete food list)
    ]

def personalized_recommendations_survey():
    st.title("Personalized Recommendations Survey")

    st.write("1. How's your mood today?")
    mood_options = ["Happy", "Lazy", "Bored", "Stressed", "Depressed", "Hungry", "None"]
    mood = st.radio("Select your mood:", mood_options)

    st.write("2. On any given day, which cuisine do you prefer?")
    cuisine_options = ["Beverage", "Japanese", "Snack", "French", "Indian", "Dessert", "Mexican", "Healthy Food", "Chinese", "Italian"]
    cuisine = st.checkbox("Select your cuisine:", cuisine_options)
    
    st.write("3. Do you have any food allergies? If yes, then do select all the items you're allergic to")
    allergy_options = ["Not Allergic to any food item", "Peanut/Tree Nuts", "Seafood", "Dairy", "Eggs", "Gluten", "Soy", "Fruits and Vegetables", "Seeds"]
    allergies = st.checkbox("Enter or select allergy:", allergy_options)
    allergy_information = st.text_area("Other:")

    foods = get_food_items()

    st.write("Select 3 food items to rate:")
    selected_food1 = st.selectbox("Select the food item (Food Item 1)", foods)
    rating1 = st.slider("How would you rate this food item?", min_value=1, max_value=10, step=1)

    selected_food2 = st.selectbox("Select the food item (Food Item 2)", foods)
    rating2 = st.slider("How would you rate this food item?", min_value=1, max_value=10, step=1)

    selected_food3 = st.selectbox("Select the food item (Food Item 3)", foods)
    rating3 = st.slider("How would you rate this food item?", min_value=1, max_value=10, step=1)

    submit_button = st.button("Submit")

    if submit_button:
        # You can process the survey responses here
        st.success("Survey submitted successfully!")

if __name__ == "__main__":
    personalized_recommendations_survey()
