import streamlit as st

#Streamlit UI
st.title('Power Calculator')
st.write('Enter a number to caculate its square,cube and fifth power')

#Get user input
input = st.number_input('Enter an integer',value=1,step=1)

#Calculate the results
square = input ** 2
cube = input ** 3
fith_power = input ** 5

#Display results
st.write(f"The square of {input} is: {square}")
st.write(f"The cube of {input} is: {cube}")
st.write(f"The fifth power of {input} is:{fith_power}")
