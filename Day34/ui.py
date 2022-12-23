from tkinter import * 
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizGUI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Create a Window
        self.window = Tk()
        self.window.title('did you know?')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score = Label()
        self.score.config(text='SCORE : 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=2)

        # Create a canvas that holds the question
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text='Question', 
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
            )
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)
        
        ### Row 1
        self.wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false)
        self.wrong_button.grid(row=2, column=0)

        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.true)
        self.right_button.grid(row=2, column=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.wrong_button.config(state='disabled')
            self.right_button.config(state='disabled')

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        
    def true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
