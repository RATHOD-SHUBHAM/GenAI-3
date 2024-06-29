import streamlit as st
import pandas as pd

st.title("Exploring Session State🔒")

text = """
Streamlit run from first line to last every time.

During some runs , we dont want certain variables to update - in such cases we use session state


Declare session state variable

    1. As Dictionary: st.session_state['number_of_rows'] = 10
    2. Using dot: st.session_state.number_of_rows = 10
"""

with st.expander("**📖 How to Use Session State**"):
    st.markdown(text)

if "number_of_rows" not in st.session_state:
    st.session_state['number_of_rows'] = 5

df = pd.read_csv('people-100.csv')
st.table(df.head(st.session_state['number_of_rows']))

if st.button("Hey"):
    st.balloons()

increment = st.button("Show More Column ⬆️")
if increment:
    st.session_state['number_of_rows'] += 1

decrement = st.button("Show less Column ⬇️")
if decrement:
    st.session_state.number_of_rows -= 1


st.write(st.session_state)

# st.table(df.head(st.session_state['number_of_rows']))