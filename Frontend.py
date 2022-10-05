"""
a program that stores book information:
Title, Author, Year, ISBN

user can:
View all records
Search an entry
Add entry
Update entry
Delete entry
Close the program
"""

from tkinter import *
import Backend
window = Tk()

window.wm_title('Bookstore')


def get_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def view_com():
    list1.delete(0,END)
    for row in Backend.view_all():
        list1.insert(END,row)

def search_com():
    list1.delete(0, END)
    for row in Backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_com():
    Backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def delete_com():
    Backend.delete(selected_tuple[0])


def update_com():
    Backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


"""Entry Labels"""

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)


"""Entry widgets"""

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


"""Listbox widget"""

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)


"""Scrollbar"""

scrol_b1 = Scrollbar(window)
scrol_b1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scrol_b1.set)
scrol_b1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_row)

"""Function Buttons"""

b1 = Button(window, text='View All', width=12, command=view_com)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search', width=12, command=search_com)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=add_com)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Entry', width=12, command=update_com)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Entry', width=12, command=delete_com)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close App', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
