import streamlit as st

st.title("Hello World")
st.snow()

st.write("Namaste :sunglasses:")

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

st.markdown("This is **_so_ beautiful**")
st.markdown("It is:red[red color] and boat are **:blue[blue color]** and bold")
st.markdown(":green[$\sqrt{x^2+y^2}=l$], this is pythogoros theoram :pencil:")

st.header("This is header")


code=""" def heloo:
        print('hello, guys')       """
st.code(code,language='python')




st.title("NEW")

st.write("This a line")

st.slider("This is slider:", 0,100)

st.divider()

st.text("This is between 20 to 60")


# a=input("write your age:")

# if st.button(a>18):
#     st.write('hello there')
# else:
#     st.write('Goodbye')

b=st.button("click me")
if b== True:
        st.write("You clicked me:cry:")
        st.snow()

a=st.number_input("Enter age:")
b=st.button("Clivk Me")
if a>18:
    # b==True
    st.write("Right:sunglasses:")
    st.snow()
else:
    st.balloons()

import streamlit as st
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
