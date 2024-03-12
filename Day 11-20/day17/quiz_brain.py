class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ{self.question_number}: {current_question.text}: (TRUE/FALSE)\n").lower()
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("\n\t\t\t\tThat's Correct. You earn a point !!")
            self.score += 1
        else:
            print("\n\t\t\t\tThat's Incorrect.")
        print(f"\t\t\t\tCURRENT SCORE :: {self.score}/{self.question_number}")