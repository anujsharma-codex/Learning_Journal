import streamlit as st
import pandas as pd

#Title
st.title("Streamlit Form Demo")


#Form to hold the interactive elements
with st.form(key='sample_form'):
    # Text Input
    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")

    # Date and Time Inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")

    # Selectors
    st.subheader("Date and Time Inputs")
    choice = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    gender = st.selectbox("Selext your gender", ["Male", "Female", "Other"])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])

    #Toggles and Checkboxes
    st.subheader("Toggles & Checkboxes")
    notifications = st.checkbox('Receive notifications?')
    toggle_value = st.checkbox('Enable dark mode?', value = False)

    #Submit Button for the Form
    submit_button = st.form_submit_button(label = 'Submit')
    

st.title("User Information Form")

with st.form(key="user_info_form"):   # Importat to define a form
    name = st.text_input("Enter your name: ")
    age = st.number_input("Enter your age: ")

    print(name, age)
    st.form_submit_button()           # important for making the form submit
# in a form the values are updated in the terminal and printed only when the form submit button is clicked
# but if we just remove the form lines and keep it normal like this


name = st.text_input("Enter your name: ")
age = st.number_input("Enter your age: ")
print(name, age) 


# In these boxes if we write something or update something the form reruns every single time unlike the form where it reran only when submit was clicked
# We dont want that because we will be having so many reruns
# so we just add a single submit button to rerun in the end only.

# More complex form rather than name and age variables , we make a dictionary to store values

# Simple Form Example
st.title("Simple Form example")
st.header("User Information Form")

with st.form(key = "user_info_form"):
    age = st.number_input("Enter your age: ")
    name = st.name_input("Enter your age: ")

    print(name, age)
    st.form_submit_button()  #mandatory thing for form to work

