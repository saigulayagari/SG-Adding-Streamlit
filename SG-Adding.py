import streamlit as st

# Title of the app
st.title("Fun Adding App for Toddlers")

# Prompt to the user
st.write("Let's add two numbers together!")

# Get the first number from the user
first_number = st.number_input("Enter the first number:", min_value=0, step=1)

# Get the second number from the user
second_number = st.number_input("Enter the second number:", min_value=0, step=1)

# Calculate the sum
result = first_number + second_number

# Display the result
st.write(f"The sum is: {result}")

