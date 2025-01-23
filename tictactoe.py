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
lbl1=Label(root,text="Player X won",fg="#1976D2",font=("Arial",20,"bold"))
lbl2=Label(root,text="Player O won",fg="#1976D2",font=("Arial",20,"bold"))


def checkwin():
   
    if text[0].get()==text[1].get()==text[2].get()=="O": 
        print("O Won")
    elif text[0].get()==text[1].get()==text[2].get()=="X":
        print("X Won")
    elif text[3].get()==text[4].get()==text[5].get()=="O":
        print("O Won")
    elif text[3].get()==text[4].get()==text[5].get()=="X":
        print("X Won")
    elif text[6].get()==text[7].get()==text[8].get()=="O":
        print("O Won")
    elif text[6].get()==text[7].get()==text[8].get()=="X":
        print("X Won")
    elif text[0].get()==text[3].get()==text[6].get()=="O":
        print("O Won")
    elif text[0].get()==text[3].get()==text[6].get()=="X":
        print("X Won")
    elif text[1].get()==text[4].get()==text[7].get()=="O":
        print("O Won")
    elif text[1].get()==text[4].get()==text[7].get()=="X":
        print("X Won")
    elif text[2].get()==text[5].get()==text[8].get()=="O":
        print("O Won")
    elif text[2].get()==text[5].get()==text[8].get()=="X":
        print("X Won")
    elif text[0].get()==text[4].get()==text[8].get()=="O":
        print("O Won")
    elif text[0].get()==text[4].get()==text[8].get()=="X":
        print("X Won")
    elif text[2].get()==text[4].get()==text[6].get()=="O":
        print("O Won")
    elif text[2].get()==text[4].get()==text[6].get()=="X":
        print("X Won")
    elif all(ele.get() != "" for ele in text):
        print("It's a Draw")
        return
    
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
   

b1=Button(root,bg="#87CEEB",textvariable=a,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(1)).grid(row=0,column=0)
b2=Button(root,bg="#87CEEB",textvariable=b,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(2)).grid(row=0,column=1)
b3=Button(root,bg="#87CEEB",textvariable=c,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(3)).grid(row=0,column=2)
b4=Button(root,bg="#87CEEB",textvariable=d,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(4)).grid(row=1,column=0)
b5=Button(root,bg="#87CEEB",textvariable=e,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(5)).grid(row=1,column=1)
b6=Button(root,bg="#87CEEB",textvariable=f,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(6)).grid(row=1,column=2)
b7=Button(root,bg="#87CEEB",textvariable=g,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(7)).grid(row=2,column=0)
b8=Button(root,bg="#87CEEB",textvariable=h,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(8)).grid(row=2,column=1)
b9=Button(root,bg="#87CEEB",textvariable=i,width=5,height=3,fg="#000000",font=("Arial",24,"bold"),command=lambda :click(9)).grid(row=2,column=2)
r=Button(root,text="RESULT",width=20,height=4,bg="#1976D2",fg="#FFFFFF",command=checkwin).place(x=70,y=500)
root.mainloop()
