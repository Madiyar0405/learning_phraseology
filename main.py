import streamlit as st
from phraseology.phraseology_app import main as phraseology_main
from quiz.quiz_app import run_quiz  # Corrected import statement
from mainPage.info import main as main_page

st.set_page_config(layout="wide")

page = st.sidebar.selectbox("Выберите страницу", ["Главная страница", "Фразеологизмы", "Викторина"])

if page == "Главная страница":
    main_page()
elif page == "Фразеологизмы":
    phraseology_main()
elif page == "Викторина":
    run_quiz()  # Changed to call the run_quiz function
