import streamlit as st
from app import create_curriculum

st.title("Curriculum Generator")
st.write("Curriculum is one step ahead, add subject and stadard and get your curriculum.")

with st.form("my_form"):
    st.write("Fill this form")
    std = st.selectbox("Select School Standard", ["standard 1", "standard 2", "standard 3", "standard 4", "standard 5"])
    sub  = st.text_input("Enter your Subjects: ")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        syllabus = create_curriculum(std, sub)
        st.text_area("Syllabus",syllabus, height=700)
