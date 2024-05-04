import requests
import streamlit as st

# Function to fetch data from the API
def fetch_data():
    url = "https://rapidapi.com/data"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None



st.set_page_config(page_title="MOE Learning Centre", page_icon=":::man_student:", layout="wide")


st.subheader("Hello, Welcome to MOE Learning Centre :wave:")
st.title("The Best Learning Environment for your children")
st.write("We provide various education service such as tutoring classes, consultation and academic ciriculum")
st.write(" For further inquiries > lilymoe74@gmail.com, +95 9798743047 ")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Services")
        st.write('##')
        st.write (
            """
            





"""






        )

