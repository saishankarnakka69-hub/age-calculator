from tkinter import *
from datetime import date
def age():
    # birth_month,birth_year,birth_day=input("enter your birthmonth and birth year and birth day").split()
    birth_month=int(month_entry.get())
    birth_year=int(year_entry.get())
    birth_day=int(day_entry.get())
    today=date.today()
    current_age=today.year-birth_year
    if (today.month,today.day)<(birth_month,birth_day):
        current_age-=1
    result_label.config(text=f"your current age is {current_age}{date.day}")
root=Tk()
root.title("Age calculation")
root.geometry("200x200")
Label(root,text="enter your dateof birth").pack()
Label(root,text="month").pack()
month_entry=Entry(root)
month_entry.pack()
Label(root,text="Year").pack()
year_entry=Entry(root)
year_entry.pack()
Label(root,text="Day").pack()
day_entry=Entry(root)
day_entry.pack()

label=Label(root,text="your current age")
label.pack()
button=Button(root,text="clickto calculate")
button.config(command=age)
button.pack()
result_label=Label(root,text=" ")
result_label.pack()
root.mainloop()

