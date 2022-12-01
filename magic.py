import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import time

# magic commands st.write()
# st.write can get all kinds of data types like , dataframe, string
# numeric, plot, etc

#simple st.write command
headline = "# This is a heading"
normal_text = "hello there"
italic = "_hi i am italic_"
number = 18
st.write(
    f""" 
         {headline},
         {normal_text},
         {italic}
         {number}
    """
    )
# Another way
st.write(
        """
         # this is heading
        this is paragraph

        this is _italic_

        this is __bold__

        """
        )
# pass a dataframe
data = {
    'name' : ['bashar' , 'mith' , 'jack'],
    'age' : [18,19,20]
}
df = pd.DataFrame(data,)
#show the dataframe
st.write(df)

#pass variable
x = 80
st.write("the value of x is" , x)

######### NOW we do above example as Magic Method ##########
# we dont need to called again and again st.write(). just do as normal python

# for heading, para, italic and bold and so on we first do """ string

"""
# This is a heading by magic method\n
this is a paragraph by magic method\n
this is a _italic_ method by magic method\n
this is a __bold__ method by magic method\n

"""

## declare dataframe by only call that df

df