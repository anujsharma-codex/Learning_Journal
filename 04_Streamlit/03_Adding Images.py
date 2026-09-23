# To put image on the page...
# make a folder in the same directory and name it static
# other than static wont work.

import streamlit as st

# along with streamlit we need to import os as well
import os

image_path = os.path.join(
    os.path.dirname(__file__),
    "03static",
    "BG.jpg"
)

st.image(image_path, width = 400)# getcwd stands for get current working directory
