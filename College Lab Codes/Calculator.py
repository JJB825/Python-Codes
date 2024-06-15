from tkinter import *

# expression=""

num1=num2=operator=None

def display(digit):
    # global expression
    current=result_label['text']
    new=current+str(digit)
    # expression+=str(digit) 
    # equation.set(expression)
    result_label.config(text=new)

# def preview():
#     global expression
#     preview_label.config(text=expression)
    

def cross():
    # global expression
    current=result_label['text']
    ch=current[len(current)-1]
    new=current.replace(ch,'')
    # equation.set(expression)
    # expression=new
    result_label.config(text=new)

def clear():
    # global expression
    # expression=""
    # equation.set(expression)
    result_label.config(text='')

# def evaluate():
#     global expression
#     try: 
#         # equation.set(str(round(eval(expression),2)))
#         expression=""
#     except:
#         # equation.set("Error")
#         expression=""

def get_operator(op):
    global num1,operator
    num1=float(result_label['text'])
    operator=op
    result_label.config(text='')

def get_result():
    global num1,num2,operator
    num2=float(result_label['text'])
    if operator=='+':
        result_label.config(text=str(round(num1+num2,2)))
    elif operator=='-':
        result_label.config(text=str(round(num1-num2,2)))
    elif operator=='*':
        result_label.config(text=str(round(num1*num2,2)))
    elif operator=='/':
        if num2==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(num1/num2,2)))

root=Tk()
root.title('Calculator')
root.geometry('325x407')
root.resizable(0,0)
root.config(background='cyan')

# preview_label=Label(root,text='',bg='cyan',fg='red')
# preview_label.grid(row=0,column=0,columnspan=6,pady=(10,10),padx=(10),sticky='w')
# preview_label.config(font=('Comic Sans MS',10))

result_label=Label(root,text='',bg='cyan',fg='red')
result_label.grid(row=0,column=0,columnspan=6,pady=(40,25),padx=(10),sticky='w')
result_label.config(font=('Comic Sans MS',25,'bold'))

btn7=Button(root,text='7',bg='blue',fg='white',width=5,height=2,command=lambda:display(7))
btn7.grid(row=1,column=0)
btn7.config(font=('Comic Sans MS',14))

btn8=Button(root,text='8',bg='blue',fg='white',width=5,height=2,command=lambda:display(8))
btn8.grid(row=1,column=1)
btn8.config(font=('Comic Sans MS',14))

btn9=Button(root,text='9',bg='blue',fg='white',width=5,height=2,command=lambda:display(9))
btn9.grid(row=1,column=2)
btn9.config(font=('Comic Sans MS',14))

btn_plus=Button(root,text='+',bg='blue',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btn_plus.grid(row=1,column=3)
btn_plus.config(font=('Comic Sans MS',14))

btnCancel=Button(root,text='Clear',bg='blue',fg='white',width=5,height=2,command=clear)
btnCancel.grid(row=1,column=4)
btnCancel.config(font=('Comic Sans MS',14))

btn4=Button(root,text='4',bg='blue',fg='white',width=5,height=2,command=lambda:display(4))
btn4.grid(row=2,column=0)
btn4.config(font=('Comic Sans MS',14))

btn5=Button(root,text='5',bg='blue',fg='white',width=5,height=2,command=lambda:display(5))
btn5.grid(row=2,column=1)
btn5.config(font=('Comic Sans MS',14))

btn6=Button(root,text='6',bg='blue',fg='white',width=5,height=2,command=lambda:display(6))
btn6.grid(row=2,column=2)
btn6.config(font=('Comic Sans MS',14))

btn_minus=Button(root,text='-',bg='blue',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_minus.grid(row=2,column=3)
btn_minus.config(font=('Comic Sans MS',14))

btnCE=Button(root,text='CE',bg='blue',fg='white',width=5,height=2,command=cross)
btnCE.grid(row=2,column=4)
btnCE.config(font=('Comic Sans MS',14))

btn1=Button(root,text='1',bg='blue',fg='white',width=5,height=2,command=lambda:display(1))
btn1.grid(row=3,column=0)
btn1.config(font=('Comic Sans MS',14))

btn2=Button(root,text='2',bg='blue',fg='white',width=5,height=2,command=lambda:display(2))
btn2.grid(row=3,column=1)
btn2.config(font=('Comic Sans MS',14))

btn3=Button(root,text='3',bg='blue',fg='white',width=5,height=2,command=lambda:display(3))
btn3.grid(row=3,column=2)
btn3.config(font=('Comic Sans MS',14))

btn_multiply=Button(root,text='*',bg='blue',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btn_multiply.grid(row=3,column=3)
btn_multiply.config(font=('Comic Sans MS',14))

btnNeg=Button(root,text='(-)',bg='blue',fg='white',width=5,height=2,command=lambda:display('-'))
btnNeg.grid(row=3,column=4)
btnNeg.config(font=('Comic Sans MS',14))

btnDot=Button(root,text='.',bg='blue',fg='white',width=5,height=2,command=lambda:display('.'))
btnDot.grid(row=4,column=0)
btnDot.config(font=('Comic Sans MS',14))

btn0=Button(root,text='0',bg='blue',fg='white',width=5,height=2,command=lambda:display(0))
btn0.grid(row=4,column=1)
btn0.config(font=('Comic Sans MS',14))


btnEqual=Button(root,text='=',bg='blue',fg='white',width=5,height=2,command=get_result)
btnEqual.grid(row=4,column=2)
btnEqual.config(font=('Comic Sans MS',14))

btn_divide=Button(root,text='/',bg='blue',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btn_divide.grid(row=4,column=3)
btn_divide.config(font=('Comic Sans MS',14))

root.mainloop()