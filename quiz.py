import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "London"], "answer": "Paris"},
    {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Python is a ...?", "options": ["Snake", "Programming Language", "Car", "Planet"], "answer": "Programming Language"}
]

score = 0
current_question = 0

def check_answer(selected):
    global score, current_question
    if selected == questions[current_question]["answer"]:
        score += 1
        messagebox.showinfo("Correct!", "You got it right!")
    else:
        messagebox.showerror("Wrong!", f"The correct answer was: {questions[current_question]['answer']}")
    
    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Quiz Finished", f"You scored {score} out of {len(questions)}")
        root.destroy()

def show_question():
    q = questions[current_question]
    question_label.config(text=q["question"])
    for i, option in enumerate(q["options"]):
        buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")

question_label = tk.Label(root, text="", wraplength=380)
question_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=20)
    btn.pack(pady=5)
    buttons.append(btn)

show_question()
root.mainloop()