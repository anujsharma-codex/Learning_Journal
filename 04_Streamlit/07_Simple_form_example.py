import streamlit as st
from datetime import datetime

# Simple Form Example
st.title("Simple Form example")
st.header("User Information Form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
}  # None creates and empty value

min_date = datetime(1090, 1, 1)
max_date = datetime.now()

with st.form(key = "user_info_form"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["dob"] = st.date_input("Enter your birthdate", max_value = max_date, min_value = min_date)

    submit_button = st.form_submit_button(label = "Submit", clear_on_submit = True)
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields !!!")
        else:
            st.balloons()
            st.write('### Info')
            for (key, value) in form_values.items():
                st.write(f"{key} : {value}")

# How the if submit button works...
# when the button is pressed, the program reruns, and when it reruns the state of the submit button becomes True:
# so when it becomes True it enters the if submit_button: condition and executes the code inside it

