import streamlit
import pandas as pd
import requests
import snowflake.connector

from urllib.error import URLError # this library is for error handling

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avacado Toast')

# streamlit.text("\U0001F600") --this code shows a smiley face emoji

streamlit.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:') 
# streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas as pd  -- Moved to the top to better organize the code
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

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
     fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
     return fruityvice_normalized      
#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
# this addas a text entry box and sends the input to Fruityvice as Part of the API Call
     # most current revision put the try: and if statements in and here is the lesson verbiage: 
             # Introducing this structure allows us to separate the code that is loaded once from 
             # the code that should be repeated each time a new value is entered. Notice there are 
             # three lines of code under the ELSE. These are important steps we will be repeating. 
             # We can pull them out into a separate bit of code called a function. We'll do that next. 

 # when a fruit is entered into the text box like 'Kiwi' then here is the sequence of events
     # 1 - Kiwi gets set as fruit_choice
     # 2 - fruit_choice now returns the first if condition as false and skips to the else clause
     # 3 - fruit_choice = 'Kiwi' gets set into the local variable this_fruit_choice = 'Kiwi' and runs through the function above get_fruityvice_data
     # 4 - the return data from the function gets set into fruityvice_normalized which then is set into back_from_function as the result of the get_fruityvice_data
     # 5 - back_from_function then feeds into the streamlit.dataframe(back_from_function) where it's displayed on the app
     
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
  else:
     back_from_function = get_fruityvice_data(fruit_choice)
     streamlit.dataframe(back_from_function)
     
except URLError as e:
      streamlit.error()
      
streamlit.write('The user entered', fruit_choice)

# import requests  -- Moved to the top to better organize the code
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") # hard coded fruit value before creating the user input variable
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) -- Moved above into the if statement.
#streamlit.text(fruityvice_response) this showed <Response [200]> in the app
# streamlit.text(fruityvice_response.json()) -- this just writes the data to the screen

# take the json version of the response and normalize it
# fruityvice_normalized = pd.json_normalize(fruityvice_response.json()) -- Moved above into the if statement.
# output it to the screen as a table
# streamlit.dataframe(fruityvice_normalized) -- Moved above into the if statement.

# while troubleshooting this will stop the app from running anything past here
streamlit.stop()

# The requirements.txt file you just added to your project tells Streamlit what libraries you plan to use in your project so it can add them in advance.
# The line shown below will tell this py file to use the library you added to the project. 
# import snowflake.connector  -- Moved to the top to better organize the code

# Let's query our trial account metadata
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# Now Let's Query Some Data, Instead of looking at metadata
streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("SELECT * FROM fruit_load_list")
          return my_cur.fetchall()
    
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List')
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list():
     streamlit.dataframe(my_data_rows)  # updated the variable from my_data_row

     # my_data_rows = my_cur.fetchall()   -- this is now old code that got changed when the 
                                             # new function get_fruit_load_list was created 
                                             # and the button generated this. The old comment was:  
                                             # changed the variable from my_data_row and the function my_cur.fetchone() 
                                             # which returns just one row to fetchall()


# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
