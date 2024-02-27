import streamlit as st
import json

# Load questions from JSON file
with open("quiz/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

# Function to display question and get user's answer
def display_question(question):
    st.write(question['question'])
    user_choice = st.radio("Выберите один из вариантов:", question['choices'], index=None)  
    question['user_choice'] = user_choice  
    return question

# Display the quiz
def run_quiz():
    st.title("Квиз по русским поговоркам и выражениям")
    total_questions = len(questions)
    correct_answers = 0
    user_answers = []

    for i, question in enumerate(questions, 1):
        st.write(f'Вопрос {i}/{total_questions}:')
        updated_question = display_question(question)
        user_answers.append(updated_question)

    submit = st.button("Подтвердить ответы")

    if submit:
        st.title("Правильные ответы")
        for i, question in enumerate(user_answers, 1):
            if question['user_choice'] == question['answer']:
                st.write(f"Вопрос {i}: Правильно!")
                correct_answers += 1
            else:
                st.write(f"Вопрос {i}: Неправильно. Правильный ответ: {question['answer']}")

        st.write(f"Вы ответили правильно на {correct_answers} из {total_questions} вопросов.")

# Run the quiz
run_quiz()


