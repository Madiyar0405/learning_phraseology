import streamlit as st

def main():

    

    st.title("Фразеологизм")

    # Описание фразеологизма с изображением (уменьшенный размер и центрирование с использованием CSS-стилей)
    st.markdown(
        "<style> .stImage {width: 300px !important; height: auto !important; display: block; margin-left: auto; margin-right: auto;} </style>",
        unsafe_allow_html=True
    )

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("https://cdn-user84060.skyeng.ru/uploads/60c1b1d0c4acd816365493.png" , width = 400)


    # Текст о фразеологизмах
    st.header("""
    # dlsanld
    Крылатые фразы не умеют летать буквально, зато своим образным полетом они делают речь интереснее и динамичнее. Чтобы не сидеть сложа руки и разгрызть гранит науки, разберемся, что же такое фразеологизм в русском языке.
    """)

    # Разделительная линия
    st.markdown("---")

    # Заголовок для раздела с определением фразеологизма
    st.header("Определение фразеологизма")

    # Описание определения фразеологизма
    st.write("""
    В лексике русского языка есть не только отдельные слова, которые помогают описывать окружающую действительность, 
    но и словосочетания, которые называют фразеологизмами. Например:
    
    - реветь белугой — громко и долго плакать;
    - задеть за живое — вызвать переживания, оскорбить самолюбие;
    - играть в жмурки — обмануть, утаить истинные намерения.
    
    На примерах видно, что значение фразеологизма не связано со смыслом каждого отдельного слова в его составе. 
    Все они меняют свои свойства: лексическое значение, форму изменения, синтаксическую функцию. 
    И все же связь между словами в составе фразеологизма неразделимая.
    
    Фразеологизмы — это устойчивые выражения из двух и более слов. 
    Они отлично живут в нашей культуре, при этом их невозможно дословно перевести на другие языки — 
    для иностранца такой перевод будет звучать странно и непонятно.
    """)

    # Изображение для примера (уменьшенный размер и центрирование с использованием CSS-стилей)
    st.markdown(
        "<style> .stImage {width: 300px !important; height: auto !important; display: block; margin-left: auto; margin-right: auto;} </style>",
        unsafe_allow_html=True
    )
    st.image("https://cdn-user84060.skyeng.ru/uploads/60c1b1d13e2ee267114519.png",  
             width = 500)
    



if __name__ == "__main__":
    main()
