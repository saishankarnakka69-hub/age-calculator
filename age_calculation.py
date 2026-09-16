#calculating the age using tkinter
from tkinter import *
def age_calculate():
    age=int(entry.get())
    if age>18:
        vote_post.config(text="you are eligible for voting")
    else:
        vote_post.config(text="NO you are not eligible for voting")
    
root=Tk()
root.title("AGE CALCULATOR")
root.geometry("500x500")
Label(root,text="enter age").pack()

entry=Entry(root)
entry.pack()
button=Button(root,command=age_calculate,text="click me").pack()
vote_post=Label(root,text="")
vote_post.pack()
root.mainloop()