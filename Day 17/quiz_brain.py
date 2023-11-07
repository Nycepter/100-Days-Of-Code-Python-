import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class QuizBrain():

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q:{self.question_number}, {current_question.text} (True/False?)\n> ").lower()
        correct_answer = current_question.answer.lower()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 100
            if self.still_has_questions() == False:
                print(f"You win! your ending score is: {self.score}")

        else:
            print("Incorrect, you lose.")
            print(f"Your score was: {self.score}")
            exit()
