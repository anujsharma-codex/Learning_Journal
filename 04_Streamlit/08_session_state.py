import streamlit as st

# A simple counter variable, without session state
counter = 0

st.write(f"Counter Value: {counter}")

# Button to increment the counter
if st.button("Increment Counter"):
    counter +=1
    st.write(f"Counter increment to {counter}")
else:
    st.write(f"Counter stays at {counter}")


""" 
# problem here: 
when we press the increment counter button, what happens is that the code reruns and the counter value set to 0 everytime rerun happens
so like even when the increment counter button presses, it becomes true, rerun happens, counter set to 0, then counter +1 happens i.e. = 1.
and that is printed everytime...
so basically increment counter here means setting the counter = 0

to fix that we use sessin state
"""
# Session State
if "counter" not in st.session_state:
    st.session_state.counter = 0       # kind of dictionary key value pair assigning.

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

else:
    st.write(f"Counter did not reset")

st.write(f"Counter Value: {st.session_state.counter}")

"""
Here now the session state is applies...
It is something that we can use to store values within the same use session.

Session is specific to each user and specific to instance of the web browser or the tab that they have open.
like a session is reset only when the page reload button is clicked or maybe a user signs in to his account to use the page... etc.
so each session is per user per run.
it dosent change when the streamlit page is rerun, but when the user refreshes the browser page.

So basically, session is a space where some values can be stored which wont change or get affected on rerunning the streamlit page.
"""