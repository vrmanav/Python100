from os import system
from time import sleep
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
#* Create Question objects which contains text, answer, and append it in question bank
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    # Create question object with question's text & answer passed as input to __init__ method
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.ask_question()


print(f"\nYou've completed the quiz!. Your final score is {quiz_brain.score}/{len(question_bank)}")