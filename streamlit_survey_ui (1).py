import streamlit as st

def personalized_recommendations_survey():
    st.title("Personalized Recommendations Survey")

    st.write("1. How's your mood today?")
    mood_options = ["Happy", "Lazy", "Bored", "Stressed", "Depressed", "Hungry", "None"]
    mood = st.radio("Select your mood:", mood_options)

    st.write("2. On any given day, which cuisine do you prefer?")
    cuisine_options = ["Beverage", "Japanese", "Snack", "French", "Indian", "Dessert", "Mexican","Healthy Food","Chinese","Italian"]
    cuisine = st.checkbox("Select your cuisine:", cuisine_options)
    
    st.write("3. Do you have any food allergies? If yes, then do select all the items you're allergic to")
    allergy_options = ["Not Allergic to any food item", "Peanut/Tree Nuts", "Seafood", "Dairy", "Eggs", "Gluten", "Soy","Fruits and Vegetables","Seeds","Italian"]
    cuisine = st.checkbox("Enter or select allergy:", allergy_options)
    allergy_information = st.text_area("Other:")

    foods=['chicken minced salad',
       'japanese curry arancini with barley salsa',
       'baked multigrain murukku', 'baked namak para',
       'spinach and feta crepes', 'mixed berry & banana smoothie',
       'khichdi', 'steam bunny chicken bao', 'meat lovers pizza',
       'chicken parmigiana with tomato sauce',
       'caramelized sesame smoked almonds', 'detox haldi tea',
       'grilled lemon margarita', 'filter coffee',
       'peri peri chicken satay', 'chicken biryani',
       'buldak (hot and spicy chicken)', 'spicy chicken masala',
       'chilli chicken', 'chicken tenders',
       'chicken and mushroom lasagna', 'chicken roulade',
       'chicken shami kebab', 'fish with white sauce',
       'chettinad fish fry', 'spanish fish fry', 'green cucumber shots',
       'veg fried rice', 'chicken paella', 'vegetable pulao',
       'vegetable bruschetta', 'egg and cheddar cheese sandwich',
       'egg in a blanket', 'kaju katli', 'mixed vegetable soup',
       'chocolate lava cake', 'gulab jamun', 'assorted rice kheer sushi',
       'dry fruit cake', 'vegetable manchurian',
       'baked wild berry cheesecake', 'mexican pizza', 'fruit cube salad',
       'veg hakka noodles', 'pasta in cheese sauce', 'butter chicken',
       'chicken tikka masala', 'Channa Masala', 'Jeera Alu',
       'Garlic Naan', 'Egg Curry with Tomatoes and Cilantro',
       'Prawn katsu Curry', 'Sweet and Sour Chicken Fried Rice',
       'Fresh Corn Tortillas']
    
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
