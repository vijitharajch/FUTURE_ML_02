import streamlit as st
import pickle

category_model = pickle.load(open('category_model.pkl', 'rb'))
priority_model = pickle.load(open('priority_model.pkl', 'rb'))

st.title("AI Support Ticket Classifier")

ticket = st.text_area("Enter Support Ticket")

if st.button("Predict"):

    category = category_model.predict([ticket])[0]

    priority = priority_model.predict([ticket])[0]

    st.write("Category:", category)

    st.write("Priority:", priority)