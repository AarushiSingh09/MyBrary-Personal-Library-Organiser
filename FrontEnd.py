

from tkinter import *
import BackEnd

def get_selected_row(event):
    global selected_tuple
    index=show.curselection()[0]
    selected_tuple=show.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    show.delete(0,END)
    for row in BackEnd.View():
        show.insert(END,row)

def search_command():
    show.delete(0,END)
    for row in BackEnd.Search(title_text.get(),author_text.get(),Issue_text.get(),Return_text.get()):
        show.insert(END,row)

def add_command():
    show.delete(0,END)
    BackEnd.Insert(title_text.get(),author_text.get(),Issue_text.get(),Return_text.get())
    show.insert(END,(title_text.get(),author_text.get(),Issue_text.get(),Return_text.get()))

def update_command ():
    show.delete(0,END)
    BackEnd.Update(selected_tuple[0],title_text.get(),author_text.get(),Issue_text.get(),Return_text.get())

def delete_command():
    show.delete(0,END)
    BackEnd.Delete(selected_tuple[0])

def fine_command():
    show.delete(0,END)
    show.insert(END,BackEnd.Fine_Generator(selected_tuple[0],Fine_text.get()))

def meaning_command():
    show.delete(0,END)
    block=BackEnd.Find_Meaning(Word_text.get())
    for item in block:
        show.insert(END,item)

window=Tk()

window.wm_title("Book_Scheduler")
l1=Label(window,text="Title")
l1.grid(row=0, column=0)

l2=Label(window,text=" Author")
l2.grid(row=0, column=2)

l3=Label(window,text="Issue Date")
l3.grid(row=1, column=0)

l4=Label(window,text="Return Date")
l4.grid(row=1, column=2)

l5=Label(window,text="Fine/Day")
l5.grid(row=2, column=0)

l6=Label(window,text="Word")
l6.grid(row=2, column=2)

title_text=StringVar()
e1=Entry(window, textvariable= title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window, textvariable= author_text)
e2.grid(row=0,column=3)

Issue_text=StringVar()
e3=Entry(window, textvariable= Issue_text)
e3.grid(row=1,column=1)

Return_text=StringVar()
e4=Entry(window, textvariable= Return_text)
e4.grid(row=1,column=3)

Fine_text=IntVar()
e5=Entry(window,textvariable=Fine_text)
e5.grid(row=2,column=1)

Word_text=StringVar()
e6=Entry(window,textvariable=Word_text)
e6.grid(row=2,column=3)

show=Listbox(window, height=12, width=40)
show.grid(row=3,column=0,rowspan=8, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=8)

show.configure(yscrollcommand=sb1.set)
sb1.configure(command=show.yview)
show.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text="View All",width=12, command=view_command)
b1.grid(row=3,column=3)

b2=Button(window, text="Search Entry",width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window, text="Add Entry",width=12,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window, text="Update Entry",width=12,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window, text="Delete Entry",width=12,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window, text="Generate Fine",width=12,command=fine_command)
b6.grid(row=8,column=3)

b7= Button(window, text="Search Meaning", width=12, command=meaning_command)
b7.grid(row=9,column=3)

b8=Button(window, text="Close",width=12,command=window.destroy)
b8.grid(row=10,column=3)

window.mainloop()
