import streamlit as st

# Typing anything:
st.write("Hello World 123456")  # this writes things on the page
st.write({"key" : "value"})
st.write(True)
3+4   # just writting an expression is automatically shown on screen the result : 7

"hello world"
"Hello World" if True else "Bye"

# Buttons and their Functioning
pressed1 = st.button("1st Button")
print("First:", pressed1)

pressed2 = st.button("2nd Button")
print("Second:", pressed2)

# When i the page loads, the button return value is set to false
# when i press the button, basically the page reloads and then returns the value True
# suppose there is second button, now when i click the second button, the page reloads and the first button value is returned as false
# but the return value of the second button is true