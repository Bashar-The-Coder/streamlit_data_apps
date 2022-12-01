import streamlit as st
from data.car_detail import *

"""
#### create a slider
"""
x   = st.slider("select car from price range" , 0, 180000, 1000) # label, min , max, step
df  = df[df['selling_price']>x] # here x is main variable intenger
#show dataframe
st.write(x)
df
len = len(df['selling_price'])
#show how many cars found
st.write(f"total __{len}__ car's found")

# 2. Text Input
# The simplest way to get user input be it some URL input
#  or some text input for sentiment analysis. It just needs a
#  single label for naming the textbox.
car_owner_type = st.text_input('Enter car owner type')
if car_owner_type:
    df_car_owner = df[df['owner']==car_owner_type]
    df_car_owner
else:
    """ nothing input """

# 3. Checkbox
# One use case for checkboxes is to hide or show/hide a 
# specific section in an app. Another could be setting up 
# a boolean value in the parameters for a function.st.checkbox()
# takes a single argument, which is the widget label. In this app,
#  the checkbox is used to toggle a conditional statement.

if st.checkbox('Show dataframe'):
    st.write(df)

# We can use st.selectbox to choose from a series
#  or a list. Normally a use case is to use it as a 
#  simple dropdown to select values from a list.

option = st.sidebar.selectbox(
    'Which seller type you want to show',
     df['seller_type'].unique())
df_seller_type = df[df['seller_type']  == option]
df_seller_type

# 5. MultiSelect
# We can also use multiple values from a dropdown.
#  Here we use st.multiselect to get multiple values as
#   a list in the variable options

# So much for understanding the important widgets.
# Now, we are going to create a simple app using multiple widgets at once.
# To start simple, we will try to visualize our football data using streamlit.
# It is pretty much simple to do this with the help of the above widgets.

options = st.sidebar.multiselect(
 'What are your favorite clubs?', df['seller_type'].unique())
st.write('You selected:', options)



seller_types = st.sidebar.multiselect('Show seller type', df['seller_type'].unique())
fuels = st.sidebar.multiselect('Show fuel type', df['fuel'].unique())
# Filter dataframe here isin passed list item
new_df = df[(df['seller_type'].isin(seller_types)) & (df['fuel'].isin(fuels))]
# write dataframe to screen
st.write(new_df)

fig = st.sidebar.line_chart(new_df, x ='seller_type',y='fuel')
# Plot!
#######Caching
# In our simple app. We read the pandas dataframe 
# again and again whenever a value changes. While
#  it works for the small data we have, it will not work
#   for big data or when we have to do a lot of processing 
#  on the data. Let us use caching using the st.cache decorator
#  function in streamlit like below.

# df = st.cache(pd.read_csv)("football_data.csv")

# Or for more complex and time taking functions 
# that need to run only once(think loading big Deep Learning models), using:
@st.cache
def complex_func(a,b):
    # DO SOMETHING COMPLEX
    return a**b
    pass
# Won't run again and again.
com = complex_func(5,2)
st.write(com)
# When we mark a function with Streamlit’s cache decorator, 
# whenever the function is called streamlit checks the
# input parameters that you called the function with.

# If this is the first time Streamlit has seen these params,
#  it runs the function and stores the result in a local cache.
# When the function is called the next time, if those params have not changed, 
# Streamlit knows it can skip executing the function 
# altogether. It just uses the results from the cache.


# For a cleaner look based on your preference, 
# you might want to move your widgets into a sidebar,
#  something like Rshiny dashboards. 
# This is pretty simple. Just add st.sidebar in your widget’s code.