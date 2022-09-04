from tkinter import *


def btnClick(number):
	global val
	val = val +str(number)
	value.set(val)
	
def clear():
	global val
	val=""
	value.set("")
	
def btn_equal():
	global val
	result = str(eval(val))
	value.set(result)


root = Tk()
root.config(bg="black")
#	===== for display ====

val=""
value=StringVar()

try:
	display=Entry(root,textvariable=value,justify="right",bg="black",fg="white",bd= 29,width=15,font=("ariel",20,"bold")).place(x=0,y=0)
except ValueError:
	print("invalid!")


# ===== row1 buttons ======

btn7 =Button(root,text='7',bg="black",fg='white',font=('ariel',30,"bold"),command=lambda: btnClick(7),bd=15).place(x=10,y=160)
btn8 =Button(root,text='8',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(8)).place(x=180,y=160)
btn9 =Button(root,text='9',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(9)).place(x=350,y=160)
btn_add =Button(root,text='+',bg='black',fg="yellow",font=('ariel',30,"bold"),bd=15,command=lambda: btnClick('+')).place(x=550,y=160)

# ===== row2 buttons ======

btn4 =Button(root,text='4',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(4)).place(x=10,y=355)
btn5 =Button(root,text='5',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(5)).place(x=180,y=355)
btn6 =Button(root,text='6',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(6)).place(x=350,y=355)
btn_sub =Button(root,text='-',bg="black",fg='yellow',font=('ariel',30,"bold"),width=1,bd=15,command=lambda: btnClick('-')).place(x=550,y=355)

# ===== row3 buttons ======

btn1 =Button(root,text='1',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(1)).place(x=10,y=550)
btn2 =Button(root,text='2',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(2)).place(x=180,y=550)
btn3 =Button(root,text='3',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(3)).place(x=350,y=550)
btn_mult =Button(root,text='*',bg="black",fg='yellow',font=('ariel',30,"bold"),width=1,bd=15,command=lambda: btnClick('*')).place(x=550,y=550)

# ===== row4 buttons ======

btn_C =Button(root,text='C',bg='black',fg="red",font=('ariel',30,"bold"),bd=15,command=clear).place(x=10,y=745)
btn_equal =Button(root,text='=',font=('ariel',30,"bold"),bg='black',fg="Lime",bd=15,command=btn_equal).place(x=180,y=745)
btn0 =Button(root,text='0',bg="black",fg='white',font=('ariel',30,"bold"),bd=15,command=lambda: btnClick(0)).place(x=350,y=745)
btn_div =Button(root,text='/',bg='black',fg="yellow",font=('ariel',30,"bold"),bd=15,width=1,command=lambda: btnClick('/')).place(x=550,y=745)

root.mainloop()
