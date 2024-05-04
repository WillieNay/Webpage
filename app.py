import streamlit as st


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
            Currently, we provide basic English, Math Science clasess for various grades:
            - We follow a variety of ciriculums provided by Cambridge, Pearson, and many more
            - Other courses such as summer school, English language speaking, IT and British Council level exam focus classes.


            If you are interested, contact us for further detailed inquiries.
           """

         )
        
        st.write("[Facebook Page >](https://www.facebook.com/profile.php?id=100086756350545&mibextid=LQQJ4d)")

