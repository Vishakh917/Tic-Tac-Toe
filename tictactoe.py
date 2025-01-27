#tictactoe
from tkinter import*
root=Tk()
root.title("TIC TAC TOE")
root.geometry("600x700+600+100")
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
text=[a,b,c,d,e,f,g,h,i]
count=0
r=0
winstr=StringVar()
winstr.set("Game On")
def checkwin():
    global r
    if text[0].get()==text[1].get()==text[2].get()=="O": 
       print("O Won")
       r=1
    elif text[0].get()==text[1].get()==text[2].get()=="X":
        print("X Won")
        r=2
    elif text[3].get()==text[4].get()==text[5].get()=="O":
        print("O Won")
        r=1
    elif text[3].get()==text[4].get()==text[5].get()=="X":
        print("X Won")
        r=2
    elif text[6].get()==text[7].get()==text[8].get()=="O":
        print("O Won")
        r=1
    elif text[6].get()==text[7].get()==text[8].get()=="X":
        print("X Won")
        r=2
    elif text[0].get()==text[3].get()==text[6].get()=="O":
        print("O Won")
        r=1
    elif text[0].get()==text[3].get()==text[6].get()=="X":
        print("X Won")
        r=2
    elif text[1].get()==text[4].get()==text[7].get()=="O":
        print("O Won")
        r=1
    elif text[1].get()==text[4].get()==text[7].get()=="X":
        print("X Won")
        r=2
    elif text[2].get()==text[5].get()==text[8].get()=="O":
        print("O Won")
        r=1
    elif text[2].get()==text[5].get()==text[8].get()=="X":
        print("X Won")
        r=2
    elif text[0].get()==text[4].get()==text[8].get()=="O":
        print("O Won")
        r=1
    elif text[0].get()==text[4].get()==text[8].get()=="X":
        print("X Won")
        r=2
    elif text[2].get()==text[4].get()==text[6].get()=="O":
        print("O Won")
        r=1
    elif text[2].get()==text[4].get()==text[6].get()=="X":
        print("X Won")
        r=2
    elif all(ele.get() != "" for ele in text):
        print("It's a Draw")
        r=3
        
    if r==1:
        winstr.set("O Won")
    elif r==2:
        winstr.set("X Won")
    elif r==3:
        winstr.set(" it's a Draw")
    
user=0
def click(n):
   
    global user
    if user==0:
        if text[n-1].get()!="X" and text[n-1].get()!="O" :
           text[n-1].set("X")
           user=1
           checkwin()
        
    elif user==1:
       if text[n-1].get()!="X" and text[n-1].get()!="O" :
           text[n-1].set("O")
           user=0
           checkwin()
def exit():
    root.destroy()
    
        
    
    
    
lbl1=Label(root,textvariable=winstr,bg="black",fg="white",font=("Arial",30,"bold"))
b1=Button(root,bg="#87CEEB",textvariable=a,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(1)).grid(row=0,column=0)
b2=Button(root,bg="#87CEEB",textvariable=b,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(2)).grid(row=0,column=1)
b3=Button(root,bg="#87CEEB",textvariable=c,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(3)).grid(row=0,column=2)
b4=Button(root,bg="#87CEEB",textvariable=d,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(4)).grid(row=1,column=0)
b5=Button(root,bg="#87CEEB",textvariable=e,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(5)).grid(row=1,column=1)
b6=Button(root,bg="#87CEEB",textvariable=f,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(6)).grid(row=1,column=2)
b7=Button(root,bg="#87CEEB",textvariable=g,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(7)).grid(row=2,column=0)
b8=Button(root,bg="#87CEEB",textvariable=h,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(8)).grid(row=2,column=1)
b9=Button(root,bg="#87CEEB",textvariable=i,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(9)).grid(row=2,column=2)
exite=Button(root,bg="red",text="QUIT",width=15,height=4,fg="#000000",font=("Arial",11,"bold"),command=exit).place(x=390,y=500)

def clear():
    for z in range(9):
        text[z].set("")
    winstr.set("Game On")
    lbl1.remove()
result=Button(root,text="RESULT",font=("Arial",11,"bold"),width=15,height=4,bg="green",fg="#000000",command=checkwin).place(x=60,y=500)
clear=Button(root,text="CLEAR",font=("Arial",11,"bold"),width=15,height=4,bg="gray",fg="#000000",command=clear).place(x=225,y=500)
lbl1.place(x=370,y=200)
root.mainloop()
