THEME_COLOR = "#375362"
from customtkinter import *
from PIL import Image
from quiz_brain import QuizBrain
import requests
import html
from question_model import Question


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        set_appearance_mode("Dark")
        self.quiz=quiz_brain
        self.window = CTk()
        self.window.title("Quiz Time")
        # self.window.configure(fg_color="#375362")
        self.window.configure(padx=20, pady=20)
        

        self.score_label = CTkLabel(self.window)
        self.score_label.configure(font=("Arial", 20, "bold"), text= f"Score: {self.quiz.score}")
        self.score_label.grid(column=1, row=0)

        self.question_area = CTkCanvas(self.window, height=250, width=300)
        self.question_area.grid(column= 0, row=1, columnspan=2, pady=50)

        self.question_text = CTkTextbox(self.question_area, wrap="word", font=("Arial", 24, "italic"), height=250, width=300, padx=20, pady=20, fg_color="white", text_color="black")
        self.question_text.pack()
        self.question_text.tag_config("center", justify="center")
        self.question_text.insert("end", "", "center")

        self.correct_image_path = ("Day 34/images/true.png")
        self.correct_image = CTkImage(dark_image=Image.open(self.correct_image_path), size=(100, 100))
        self.correct_button = CTkButton(self.window, image=self.correct_image, text="", width=100, height=100, fg_color="#242424", hover_color="#404040", command=self.true_answer)
        self.correct_button.grid(column=0, row=2)
        
        self.incorrect_image_path = ("Day 34/images/false.png")
        self.incorrect_image = CTkImage(dark_image=Image.open(self.incorrect_image_path), size=(100, 100))
        self.incorrect_button = CTkButton(self.window, image=self.incorrect_image, text="", width=100, height=100, fg_color="#242424", hover_color="#404040", command=self.false_answer)
        self.incorrect_button.grid(column=1, row=2)




        self.next_question()

        self.window.mainloop()
       
    def next_question(self):
        self.question_text.configure(fg_color ="white")
        if self.quiz.still_has_questions():
            self.question_text.delete(0.0, "end")
            q_text = self.quiz.next_question()
            self.question_text.insert(0.0,q_text, "center")
        else: 
            self.question_text.delete(0.0, "end")
            self.question_text.insert(0.0,f"You have finished the Quiz! you got {self.quiz.score}/10 correct.", "center")
            self.correct_button.configure(command = exit)
            self.incorrect_button.configure(command = exit)


    def true_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.question_text.configure(fg_color ="green")
            self.score_label.configure(font=("Arial", 20, "bold"), text= f"Score: {self.quiz.score}")
        else:
            self.question_text.configure(fg_color ="red")
        self.window.after(1000, self.next_question)


  
        
            





