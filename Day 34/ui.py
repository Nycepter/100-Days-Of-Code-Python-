THEME_COLOR = "#375362"
from customtkinter import *
from PIL import Image




class QuizInterface:
    def __init__(self) -> None:
        set_appearance_mode("Dark")
        self.window = CTk()
        self.window.title("Quiz Time")
        # self.window.configure(fg_color="#375362")
        self.window.configure(padx=20, pady=20)
        

        self.score_label = CTkLabel(self.window, text="Score: 0")
        self.score_label.configure(font=("Arial", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.question_area = CTkCanvas(self.window, height=250, width=300)
        self.question_area.grid(column= 0, row=1, columnspan=2, pady=50)

        self.question_text = CTkTextbox(self.question_area, wrap="word", font=("Arial", 24, "italic"), height=250, width=300, padx=20, pady=20, fg_color="white", text_color="black")
        self.question_text.pack()
        self.question_text.tag_config("center", justify="center")
        self.question_text.insert("end", "I can't see the code in the code editor on Auditorium because it's too small.", "center")

        self.correct_image_path = ("Day 34/images/true.png")
        self.correct_image = CTkImage(dark_image=Image.open(self.correct_image_path), size=(100, 100))
        self.correct_button = CTkButton(self.window, image=self.correct_image, text="", width=100, height=100, fg_color="#242424", hover_color="#404040")
        self.correct_button.grid(column=0, row=2)
        
        self.incorrect_image_path = ("Day 34/images/false.png")
        self.incorrect_image = CTkImage(dark_image=Image.open(self.incorrect_image_path), size=(100, 100))
        self.incorrect_button = CTkButton(self.window, image=self.incorrect_image, text="", width=100, height=100, fg_color="#242424", hover_color="#404040")
        self.incorrect_button.grid(column=1, row=2)






        self.window.mainloop()
       