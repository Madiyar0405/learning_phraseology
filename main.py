import streamlit as st
from phraseology.phraseology_app import main as phraseology_main
from quiz.quiz_app import main as quiz_main
from mainPage.info import main as main_page


st.set_page_config(layout="wide")


page = st.sidebar.selectbox("Выберите страницу", ["Главная страница", "Фразеологизмы", "Викторина"])


if  page  == "Главная страница":
    main_page()
elif page == "Фразеологизмы":
    phraseology_main()
elif page == "Викторина":
    quiz_main()
