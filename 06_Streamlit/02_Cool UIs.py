import streamlit as st

st.title("Super Simple Title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is a Markdown")
st.caption("this is a captioni")

# To write code - 
code_ex = """
def greet(name):
    print("Hello", name)"""

st.code(code_ex, language= "python")

# To make divider lines e.g. -> --------
st.divider()
