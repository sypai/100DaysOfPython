class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        display_string = f"\nQ.{self.question_number + 1} {current_question.text}"
        user_answer = input(display_string + (" (True/False) ==> "))
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"Oops! It's actually {correct_answer}")
        
        print(f"Your score is: {self.score}/{self.question_number}")
        