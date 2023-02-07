import streamlit

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avacado Toast')

# streamlit.text("\U0001F600") --this code shows a smiley face emoji

streamlit.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:') 
# streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) --this puts the number of the row corresponding to the fruit
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.fruit))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
