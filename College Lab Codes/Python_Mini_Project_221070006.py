# Importing required modules

from tkinter import *
from tkinter import messagebox

import random
import time
import threading

# Declaring a set of constants

OPERATOR = ["+", "-", "*", "/"]
MIN_OPERAND = 4
MAX_OPERAND = 20
TOTAL_PROBLEMS = 10

# Function to generate the problem

def generate_problem():
    operand1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expr = str(operand1) + " " + operator + " " + str(operand2)
    answer = round(eval(expr))

    return expr,answer

# Generate the quiz

score = 0
quiz_completed = False
total_time = 0
time_limit = 60
clock = 60

def timer(time_limit):
    global quiz_completed, total_time, clock

    start_time = time.time()

    while not quiz_completed and time.time() - start_time < time_limit:
        clock -= 1
        time_lbl.config(text=f"Time left: {clock} secs")
        time.sleep(1)

    if not quiz_completed:  # If quiz hasn't been completed within the time limit
        root.after(0, end_quiz)

    end_time = time.time()
    total_time = round(end_time - start_time,2)

def start_quiz():
    global quiz_thread, timer_thread

    start_btn.place_forget()
    instructions_label.place_forget()

    time_lbl.place(x=5, y=5)
    que_lbl.place(x=20, y=170)
    question_field.place(x=20, y=220)
    ans_lbl.place(x=20, y=270)
    answer_field.place(x=20, y=320)
    feedback_lbl.place(x=225, y=370)
    next_btn.place(x=285, y=430)
    quit_btn.place(x=360, y=5)
    chk_btn.place(x=165, y=430)

    timer_thread = threading.Thread(target = timer, args = (time_limit,))
    timer_thread.start()
    quiz_thread = threading.Thread(target = generate_quiz)
    quiz_thread.start()

def check_answer():
    global score, user_ans, answer

    user_response = user_ans.get().strip()
    if user_response == str(answer):
        score += 1
        feedback_lbl.config(text="Correct", fg="blue")
    else:
        feedback_lbl.config(text="Incorrect", fg="red")

def generate_quiz():
    global answer, user_ans

    expr, answer = generate_problem()

    que_lbl.config(text="Question " + str(que_num) + ":")
    question_field.delete(0, END)  # Clearing previous content in the question field
    question_field.insert(0, expr)  # Inserting new question into the Entry widget
    feedback_lbl.config(text="")
    next_btn.config(state="disabled")

    user_ans = StringVar()
    answer_field.config(textvariable=user_ans)

    next_btn.config(state="normal")

def next_question():
    global que_num, user_ans, score

    user_ans.set("")  # Clearing user's answer field
    que_num += 1

    if que_num <= TOTAL_PROBLEMS - 1:
        generate_quiz()
    elif que_num == TOTAL_PROBLEMS:
        next_btn.config(text="Submit")
        generate_quiz()
        next_btn.config(command=end_quiz)

def end_quiz():
    global quiz_completed, quiz_thread, timer_thread
    quiz_completed = True

    quiz_thread.join()
    timer_thread.join()

    accuracy = (score * 100) // TOTAL_PROBLEMS
    messagebox.showinfo("Quiz Completed", f"Nice Work! You finished the quiz in {total_time} secs\nYour score is {score} / {TOTAL_PROBLEMS}\nAccuracy: {accuracy} %")
    root.destroy()

root = Tk() 
root.title("Math-Quiz") 
root.geometry("640x550") 
root.resizable(False, False)
root.configure(background="light green") 

tit_lbl = Label(root, text="Timed Math Quiz", font=('Great Vibes',40,'bold'),bg="light green", fg="blue")
tit_lbl.place(x=140, y=90)

instructions = ("\nInstructions:\n"
                "1. Read each question carefully before answering.\n" 
                "2. Round division answers to the nearest integer.\n"
                "3. Click the 'Start' button to begin the quiz.\n"
                "4. The quiz will end in 60 secs.\n"
                "5. Press the check button and then press next.")

instructions_label = Label(root, text=instructions, font=('Great Vibes', 30), bg="light green", fg="blue")
instructions_label.place(x=20, y=170)

start_btn = Button(root, text='Start',bg='yellow',fg='red',width=8,height=1, font=('Comic Sans MS',15, 'bold'), command=start_quiz)
start_btn.place(x=480, y=5)

time_lbl = Label(root, text="Time left: 00 secs", font=('Comic Sans MS',20), bg="light green", fg="blue")

quit_btn = Button(root, text='Quit',bg='yellow',fg='red',width=8,height=1, font=('Comic Sans MS',15, 'bold'), command=end_quiz)

que_lbl = Label(root, font=('Comic Sans MS',15), bg="light green", fg="blue")

question_field=Entry(root, width=45, bd=3, font=('Comic Sans MS',15))

ans_lbl = Label(root, text="Answer:", font=('Comic Sans MS',15), bg="light green", fg="blue")

answer_field=Entry(root, width=45, bd=3, font=('Comic Sans MS',15))

feedback_lbl = Label(root, font=('Great Vibes',30), bg="light green", fg="blue")

next_btn = Button(root, text='Next',bg='yellow',fg='red',width=8,height=1, font=('Comic Sans MS',15, 'bold'), command= next_question)

chk_btn = Button(root, text='Check',bg='yellow',fg='red',width=8,height=1, font=('Comic Sans MS',15, 'bold'), command= check_answer)

que_num=1

root.mainloop()