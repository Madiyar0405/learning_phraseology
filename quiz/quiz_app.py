# import streamlit as st
# import random

# def show_question(question_data):
#     st.write(f"**Вопрос:** {question_data['Вопрос']}")
#     random.shuffle(question_data['Ответы'])
#     selected_option = st.radio("Выберите правильный ответ:", question_data["Ответы"])
#     return selected_option

# def main():
#     st.title("Фразеологическая викторина")

#     questions = [
#         {
#             "Вопрос": "Какое значение имеет фразеологизм 'Бить баклуши'?",
#             "Ответы": ["Прогуливаться без дела", "Быть внимательным", "Пить очень много"],
#             "Правильный ответ": "Прогуливаться без дела"
#         },
#         {
#             "Вопрос": "Что означает фразеологизм 'Взять волка'?",
#             "Ответы": ["Принять на себя трудное дело", "Быть внимательным", "Пить очень много"],
#             "Правильный ответ": "Принять на себя трудное дело"
#         },
#     ]

#     score = 0

#     for i, question_data in enumerate(questions, start=1):
#         st.write(f"**Вопрос {i}:**")
#         selected_option = show_question(question_data)
#         if selected_option == question_data["Правильный ответ"]:
#             st.write("Правильно!")
#             score += 1
#         else:
#             st.write("Неправильно!")

#     st.write(f"Вы ответили правильно на {score} из {len(questions)} вопросов.")
# Фразеологические вопросы
# def show_question(questions):
#     question = questions[st.session_state.current_question] 
#     st.write(question['question'])
#     selected_choice = st.radio("Выберите ваш ответ:", question['choices']) 
#     submit_button = st.button("Отправить") 
#     if submit_button:
#         check_answer(selected_choice, questions)
#         st.session_state.show_question = False

# # Функция для проверки выбранного ответа и вывода обратной связи
# def check_answer(selected_choice, questions):
#     question = questions[st.session_state.current_question]
#     if selected_choice == question["answer"]:
#         st.write("Верно!")
#         st.balloons()
#         st.session_state.score += 1
#     else:
#         st.write("Неверно!")
#     next_question(questions)

# # Функция для перехода к следующему вопросу
# def next_question(questions):
#     current_question = st.session_state.current_question + 1
#     if current_question < len(questions): 
#         st.session_state.current_question = current_question 
#         st.session_state.show_question = True 
#     else:
#         st.success("Викторина завершена! Ваш счет: {}/{}".format(st.session_state.score, len(questions)))
#         st.session_state.show_question = False  # Сбрасываем переменную состояния после завершения викторины

# # Главная функция - инициализация трех переменных состояния сеанса.
# def main():
#     phraseology_questions = [
#         {
#             "question": "Что означает фразеологизм 'бить баклуши'?",
#             "choices": ["Не выполнять обещания", "Быть очень ловким", "Любить красивые вещи"],
#             "answer": "Не выполнять обещания"
#         },
#         {
#             "question": "Какое значение имеет фразеологизм 'вешать лапшу на уши'?",
#             "choices": ["Говорить неправду", "Быть очень умным", "Быть очень смелым"],
#             "answer": "Говорить неправду"
#         }
#     ]

#     if 'current_question' not in st.session_state:
#         st.session_state.current_question = 0 
#     if 'score' not in st.session_state:
#         st.session_state.score = 0
#     if 'show_question' not in st.session_state:
#         st.session_state.show_question = True

#     st.title("Фразеологическая викторина")

#     if st.session_state.show_question:
#         show_question(phraseology_questions)
#     else:
#         st.session_state.show_question = True  # Обнуляем переменную состояния перед вызовом следующего вопроса
#         next_question(phraseology_questions)

# if __name__ == "__main__":
#     main()





def load_questions():
    with open("quiz/questions.json", "r", encoding="utf-8") as file:
        question_list = json.load(file)
    return question_list


# Python imports
import json
from typing import Type, Union, Dict, Any, List
import random
from urllib.request import urlopen

# 3rd party imports
import streamlit as st

# Load questions from JSON file
def load_questions_from_file():
    with open("quiz/questions.json", 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions

# Map questions to choices
index_map = {0: "A: ", 1: "B: ", 2: "C: " , 3: "D"}

def gen_quiz(question_obj, question_number, key="my-form"):
    ans_list = question_obj["choices"]
    original_order = question_obj.get("original_order", None)  # Получаем сохраненный порядок ответов, если есть
    correct_answer = question_obj["answer"]  # Правильный ответ
    exp_list = []

    q_string = question_obj["question"]

    # Если сохраненный порядок ответов доступен, используем его, иначе случайным образом перемешиваем варианты ответов
    if original_order:
        choice_list = [index_map[i] + ans_list[i] for i in original_order]
    else:
        choice_list = [index_map[i] + choice for i, choice in enumerate(ans_list)]
        random.shuffle(choice_list)

    selected_index = st.radio(q_string, choice_list, index=0, key=key)  # Устанавливаем индекс по умолчанию

    submit = st.form(key=key).form_submit_button("Submit")

    if submit:
        correct_index = ans_list.index(correct_answer)
        if original_order:
            selected_index = original_order[int(selected_index)]  # Преобразуем индекс обратно в исходный порядок, если он был сохранен
        else:
            selected_index = int(selected_index)  # Преобразуем в целое число
        if selected_index == correct_index:
            st.success("Correct! " + choice_list[selected_index])
        else:
            st.error("Wrong! " + choice_list[selected_index])
            # Показываем правильный ответ
            st.write("Correct answer: " + choice_list[correct_index])

    # Показываем объяснения, если доступно
    with st.expander("Explanations"):
        for index, item in enumerate(exp_list):
            if original_order:
                st.write(index_map[original_order[index]] + ans_list[original_order[index]] + " - " + item)
            else:
                st.write(index_map[index] + ans_list[index] + " - " + item)


prev_question_number = None
prev_question = None

def app(questions: List[Dict[str, Any]]) -> None:
    global prev_question_number, prev_question

    # Randomize questions
    random.shuffle(questions)

    curr_question_number = st.number_input(
        "Question Number:", min_value=0, max_value=len(questions) - 1, value=0
    )

    # Проверяем, изменился ли номер вопроса
    if curr_question_number != prev_question_number:
        prev_question_number = curr_question_number
        prev_question = questions[curr_question_number]

    # Get question details
    question = prev_question

    # Generate the quiz
    gen_quiz(question, curr_question_number)


def main() -> None:
    # Load questions from file
    questions = load_questions_from_file()
    app(questions)


if __name__ == "__main__":
    main()
