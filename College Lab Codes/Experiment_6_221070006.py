from tkinter import *

expression = "" 

def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 

def equalpress(): 
	try: 
		global expression 
		total = str(round(eval(expression),2)) 
		equation.set(total) 
		expression = "" 
 
	except: 
		equation.set(" error ") 
		expression = "" 
 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
	
def cross():
    global expression
    ch=expression[len(expression)-1]
    expression=expression.replace(ch,'')
    equation.set(expression)
 
   
gui = Tk() 
gui.configure(background="light green") 
gui.title("Simple Calculator") 
gui.geometry("335x350") 
equation = StringVar() 

expression_field = Entry(gui, textvariable=equation) 
expression_field.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky='w')
expression_field.config(font=('Comic Sans MS',20,'bold'))

button1 = Button(gui, text='1',bg='blue',fg='white',width=5,height=2, command=lambda: press(1)) 
button1.grid(row=3, column=0) 
button1.config(font=('Comic Sans MS',14))

button2 = Button(gui, text='2',bg='blue',fg='white',width=5,height=2, command=lambda: press(2)) 
button2.grid(row=3, column=1) 
button2.config(font=('Comic Sans MS',14))

button3 = Button(gui, text='3',bg='blue',fg='white',width=5,height=2, command=lambda: press(3)) 
button3.grid(row=3, column=2) 
button3.config(font=('Comic Sans MS',14))

multiply = Button(gui, text='*',bg='blue',fg='white',width=5,height=2, command=lambda: press("*")) 
multiply.grid(row=3, column=3) 
multiply.config(font=('Comic Sans MS',14))

button4 = Button(gui, text='4',bg='blue',fg='white',width=5,height=2, command=lambda: press(4)) 
button4.grid(row=2, column=0) 
button4.config(font=('Comic Sans MS',14))

button5 = Button(gui, text='5',bg='blue',fg='white',width=5,height=2, command=lambda: press(5)) 
button5.grid(row=2, column=1) 
button5.config(font=('Comic Sans MS',14))

button6 = Button(gui, text='6',bg='blue',fg='white',width=5,height=2, command=lambda: press(6)) 
button6.grid(row=2, column=2) 
button6.config(font=('Comic Sans MS',14))

minus = Button(gui, text='-',bg='blue',fg='white',width=5,height=2, command=lambda: press("-")) 
minus.grid(row=2, column=3) 
minus.config(font=('Comic Sans MS',14))

btnCE = Button(gui, text='CE',bg='blue',fg='white',width=5,height=2, command=cross) 
btnCE.grid(row=2, column=4) 
btnCE.config(font=('Comic Sans MS',14))

button7 = Button(gui, text='7',bg='blue',fg='white',width=5,height=2, command=lambda: press(7)) 
button7.grid(row=1, column=0) 
button7.config(font=('Comic Sans MS',14))

button8 = Button(gui, text='8',bg='blue',fg='white',width=5,height=2, command=lambda: press(8)) 
button8.grid(row=1, column=1) 
button8.config(font=('Comic Sans MS',14))

button9 = Button(gui, text='9',bg='blue',fg='white',width=5,height=2, command=lambda: press(9)) 
button9.grid(row=1, column=2) 
button9.config(font=('Comic Sans MS',14))

plus = Button(gui, text='+',bg='blue',fg='white',width=5,height=2, command=lambda: press("+")) 
plus.grid(row=1, column=3) 
plus.config(font=('Comic Sans MS',14))

btnclr = Button(gui, text='Clear',bg='blue',fg='white',width=5,height=2, command=clear) 
btnclr.grid(row=1, column=4)
btnclr.config(font=('Comic Sans MS',14))

Decimal= Button(gui, text='.',bg='blue',fg='white',width=5,height=2, command=lambda: press('.')) 
Decimal.grid(row=4, column=0) 
Decimal.config(font=('Comic Sans MS',14))

button0 = Button(gui, text='0',bg='blue',fg='white',width=5,height=2, command=lambda: press(0)) 
button0.grid(row=4, column=1) 
button0.config(font=('Comic Sans MS',14))

divide = Button(gui, text='/',bg='blue',fg='white',width=5,height=2, command=lambda: press("/")) 
divide.grid(row=4, column=2) 
divide.config(font=('Comic Sans MS',14))

equal = Button(gui, text='=',bg='blue',fg='white',width=5,height=2, command=equalpress) 
equal.grid(row=4, column=3) 
equal.config(font=('Comic Sans MS',14))

gui.mainloop() 
