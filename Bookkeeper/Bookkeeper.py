from tkinter import *
import backend


def get_selected_row(event):
    """To select the items in the list box"""
    global selected_row
    index = li.curselection()[0]
    selected_row = li.get(index)

    book_entry.delete(0, END)
    book_entry.insert(END, selected_row[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_row[2])
    date_entry.delete(0, END)
    date_entry.insert(END, selected_row[3])


def delete_command():
    """Deleting items in the database"""
    backend.delete(selected_row[0])


def view_command():
    """Viewing all of the items in database"""
    li.delete(0, END)
    for row in backend.view():
        li.insert(END, row)


def search_command():
    """Searching for items in database"""
    li.delete(0, END)
    for row in backend.search(book_text.get(), author_text.get(), date_text.get()):
        li.insert(END, row)


def add_command():
    """Adding a items in database"""
    backend.insert(book_text.get(), author_text.get(), date_text.get())
    li.delete(0, END)
    li.insert(END, (book_text.get(), author_text.get(), date_text.get()))


def label(win):
    """Labels in the GUI"""
    book = Label(win, text="Book", fg="#d6d0d0", bg="#0f0f0f")
    book.grid(row=0, column=0)

    author = Label(win, text="Author", fg="#d6d0d0", bg="#0f0f0f")
    author.grid(row=1, column=0)

    date = Label(win, text="Date", fg="#d6d0d0", bg="#0f0f0f")
    date.grid(row=2, column=0)


def entry(win):
    """Getting input for the user using entry"""
    global book_text, book_entry, author_text, author_entry, date_text, date_entry
    book_text = StringVar()
    book_entry = Entry(win, textvariable=book_text, width=50, bg="#a3a0a0")
    book_entry.grid(row=0, column=1)

    author_text = StringVar()
    author_entry = Entry(win, textvariable=author_text, width=50, bg="#a3a0a0")
    author_entry.grid(row=1, column=1)

    date_text = StringVar()
    date_entry = Entry(win,textvariable=date_text, width=50, bg="#a3a0a0")
    date_entry.grid(row=2, column=1)


def li_sc_bar(win):
    """The scroll bar and the listbox to display the items in the database"""
    global li
    sb = Scrollbar(win)
    sb.grid(row=1, column=10, rowspan=20)
    sb2 = Scrollbar(win, orient=HORIZONTAL)
    sb2.grid(row=20, column=5)

    li = Listbox(win, yscrollcommand=sb.set, xscrollcommand=sb.set, height=15, width=35, bg="#a3a0a0")
    li.grid(row=0, column=3, rowspan=20, columnspan=5)
    li.bind('<<ListboxSelect>>', get_selected_row)

    sb.config(command=li.yview)
    sb2.config(command=li.xview)


def buttons(win):
    """Buttons for the window"""
    add_button = Button(text="Add", command=add_command, width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    add_button.grid(row=4, column=0)

    search_button = Button(text="Search", command=search_command, width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    search_button.grid(row=4, column=1)

    delete_button = Button(text="Delete", command=delete_command, width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    delete_button.grid(row=6, column=0)

    viewAll_button = Button(text="View All", command=view_command, width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    viewAll_button.grid(row=6, column=1)

    close_button = Button(text="Close", width=12, pady=5, command=win.destroy, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    close_button.place(x=100, y=170)


def main():
    win = Tk()
    win.geometry("635x260")
    win.title("Book Keeper")
    win['bg'] = "#0f0f0f"

    label(win)
    entry(win)
    li_sc_bar(win)
    buttons(win)


    win.mainloop()


if __name__ == '__main__':
    main()




