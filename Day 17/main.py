from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def Question_Bank_Init():
    Question_Bank = []
    for dict in question_data:
        question = Question(dict["text"], dict["answer"])
        Question_Bank.append(question)
    return Question_Bank


Question_Bank = Question_Bank_Init()

quiz = QuizBrain(Question_Bank)
while quiz.still_has_questions() == True:
    quiz.next_question()
print("Thank you for playing.")
