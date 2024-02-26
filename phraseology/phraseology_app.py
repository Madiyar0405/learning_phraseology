import streamlit as st
import random
import json
import re


def display_phraseology_info(info):
    st.write("Фразеологизм:", info.get("Фразеологизм"))
    st.write("Значение:", info.get("Значение"))
    st.write("Происхождение:", info.get("Происхождение", "Нет информации"))


def main():
    with open("phraseology/phraseology_data.json", "r", encoding="utf-8") as file:
        phraseology_list = json.load(file)
    
    search_term = st.text_input("Введите фразеологизм или ключевое слово для поиска")
    if st.button("Поиск"):
        for phrase_info in phraseology_list:
            phraseology = phrase_info.get("Фразеологизм", "").lower()
            if re.search(r'\b{}\b'.format(re.escape(search_term.lower())), phraseology):
                st.subheader(phrase_info["Фразеологизм"])
                display_phraseology_info(phrase_info)

    selected_letter = st.sidebar.selectbox("Выберите начальную букву для вывода фразеологизмов по алфавиту",
                                           sorted(set(phrase.get('Фразеологизм', '')[0].upper() for phrase in phraseology_list if phrase.get('Фразеологизм'))))
    filtered_phrases = [phrase_info for phrase_info in phraseology_list if phrase_info.get('Фразеологизм', '').startswith(selected_letter.lower())]
    
    for phrase_info in filtered_phrases:
        st.subheader(phrase_info["Фразеологизм"])
        display_phraseology_info(phrase_info)

    if st.button("Получить случайный фразеологизм"):
        random_phrase_info = random.choice(phraseology_list)
        st.subheader(random_phrase_info.get("Фразеологизм", "Нет информации"))
        display_phraseology_info(random_phrase_info)


if __name__ == "__main__":
    main()
