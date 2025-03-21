from os import system
from time import sleep
# TODO: asking questions
# TODO: validating the answer
# TODO: check if the quiz is over or not
class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 1
        self.question_list = question_bank
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number <= len(self.question_list)

    def check_answer(self,user_answer, correct_answer):
        return user_answer == correct_answer

    def ask_question(self):
        for question in self.question_list:
            current_question = question.text
            system('clear')
            print("WELCOME TO KAUN BANEGA CROREPATI 💰")
            user_answer = input(f"\nQ.{self.question_number}: {current_question} (True / False):\n").lower()
            if self.check_answer(user_answer, question.answer.lower()):
                print("That's correct 🎉 ",end="")
                self.score += 1
            else:
                print("That's incorrect 😕 ",end="")
            print(f"Your current score is {self.score}/{self.question_number}")
            self.question_number += 1
            sleep(1.5)

