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
my_fruit_list = my_fruit_list.set_index('Fruit')  #this puts the name of the fruit as opposed to the number of the row corresponding to the fruit in the picker list

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) this is the whole list with no default values
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries']) this creates 2 default values of fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
# streamlit.dataframe(my_fruit_list) this is the whole list of fruits
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
# this addas a text entry box and sends the input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") # hard coded fruit value before creating the user input variable
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response) this showed <Response [200]> in the app
# streamlit.text(fruityvice_response.json()) -- this just writes the data to the screen

# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

# The requirements.txt file you just added to your project tells Streamlit what libraries you plan to use in your project so it can add them in advance.
# The line shown below will tell this py file to use the library you added to the project. 
import snowflake.connector 
