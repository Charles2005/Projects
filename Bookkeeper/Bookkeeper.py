from tkinter import *
import sqlite3

win = Tk()
win.geometry("600x245")
win.title("Book Keeper")
book = Label(win, text="Book")
book.grid(row=0, column=0)

date = Label(win, text="Date")
date.grid(row=1, column=0)

author = Label(win, text="Author")
author.grid(row=2, column=0)

book_text = StringVar()
book_entry = Entry(win, textvariable=book_text, width=50)
book_entry.grid(row=0, column=1)

date_text = StringVar()
date_entry = Entry(win, textvariable=date_text, width=50)
date_entry.grid(row=1, column=1)

author_text = StringVar()
author_entry = Entry(win, textvariable=author_text, width=50)
author_entry.grid(row=2, column=1)

list = Listbox(win, height=15, width=35)
list.grid(row=0, column=3, rowspan=20, columnspan=5)

sb = Scrollbar(win)
sb.grid(row=1, column=10, rowspan=20)

list.bind("<<ListboxSelection>>",)

add_button = Button(win, text="Add", width=12, pady=5)
add_button.grid(row=4, column=0)

search_button = Button(win, text="Search", width=12, pady=5)
search_button.grid(row=4, column=1)

delete_button = Button(win, text="Delete", width=12, pady=5)
delete_button.grid(row=6, column=0)

viewAll_button = Button(win, text="View All", width=12, pady=5)
viewAll_button.grid(row=6, column=1)

close_button = Button(win, text="Close", width=12, pady=5, command=win.destroy)
close_button.place(x=100, y=170)

win.mainloop()
