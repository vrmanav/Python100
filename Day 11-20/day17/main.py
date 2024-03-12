# Day 17: Quiz game
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank  = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    q1 = Question(q_text, q_answer)
    question_bank.append(q1)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You completed the quiz. Your final score is {quiz_brain.score}/{quiz_brain.question_number}")