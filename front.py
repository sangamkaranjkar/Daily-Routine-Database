from tkinter import *
from datetime import date
import time
import back
today = date.today()
time = time.strftime("%H:%M:%S")

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    back.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for row in back.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in back.search(date_text.get(),time_text.get(),study_text.get(),hour_text.get(),note_text.get(),log_text.get()):
        list.insert(END,row)

def add_command():
    back.insert(date_text.get(),time_text.get(),study_text.get(),hour_text.get(),note_text.get(),log_text.get())

    list.delete(0,END)
    list.insert(END,(date_text.get(),time_text.get(),study_text.get(),hour_text.get(),note_text.get(),log_text.get()))



win = Tk()
win.wm_title("My Daily Routine Diary")

l1 = Label(win, text='Date :-')
l1.grid(row=0,column=0)
date_text = StringVar()
e1 = Entry(win, textvariable = date_text)
e1.grid(row=0, column= 1)
e1.delete(0, END)
e1.insert(0, str(today))

l2 = Label(win, text='Time :-')
l2.grid(row=1,column=0)
time_text = StringVar()
e2 = Entry(win, textvariable = time_text)
e2.grid(row=1, column= 1)
e2.delete(0, END)
e2.insert(0, str(time))

l3 = Label(win, text='Topic of Study:-')
l3.grid(row=0,column=2)
study_text = StringVar()
e3 = Entry(win, textvariable = study_text)
e3.grid(row=0, column= 3)

l4 = Label(win, text="How many hour's?:-")
l4.grid(row=1,column=2)
hour_text = StringVar()
e4 = Entry(win, textvariable = hour_text)
e4.grid(row=1, column= 3)

l5 = Label(win, text="Note :-")
l5.grid(row=2,column=0)
note_text = StringVar()
e5 = Entry(win, textvariable = note_text)
e5.grid(row=2, column= 1)

l6 = Label(win, text="Today's log :-")
l6.grid(row=2,column=2)
log_text = StringVar()
e6 = Entry(win, textvariable = log_text)
e6.grid(row=2, column= 3)

b1 = Button(win,text='ADD',width=12,pady=5,command= add_command)
b1.grid(row=4,column=0)

b2 = Button(win,text='Search',width=12,pady=5,command= search_command)
b2.grid(row=4,column=1)

b3 = Button(win,text='Delete date',width=12,pady=5, command= delete_command)
b3.grid(row=4,column=2)

b4 = Button(win,text='View all',width=12,pady=5, command= view_command)
b4.grid(row=4,column=3)

b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b5.grid(row=5,column=3)


list = Listbox(win,height=8,width=60)
list.grid(row=5,column=0,rowspan=9,columnspan=3)

sb = Scrollbar(win)
sb.grid(row=6,column=3,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)







win.mainloop()
