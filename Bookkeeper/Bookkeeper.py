from tkinter import *
import sqlite3



def label(win):
    book = Label(win, text="Book", fg="#d6d0d0", bg="#0f0f0f")
    book.grid(row=0, column=0)

    date = Label(win, text="Date", fg="#d6d0d0", bg="#0f0f0f")
    date.grid(row=1, column=0)

    author = Label(win, text="Author", fg="#d6d0d0", bg="#0f0f0f")
    author.grid(row=2, column=0)


def entry(win):
    book_text = StringVar()
    book_entry = Entry(win, textvariable=book_text, width=50, bg="#a3a0a0")
    book_entry.grid(row=0, column=1)

    date_text = StringVar()
    date_entry = Entry(win, textvariable=date_text, width=50, bg="#a3a0a0")
    date_entry.grid(row=1, column=1)

    author_text = StringVar()
    author_entry = Entry(win, textvariable=author_text, width=50, bg="#a3a0a0")
    author_entry.grid(row=2, column=1)


def list_box(win):
    li = Listbox(win, height=15, width=35, bg="#a3a0a0")
    li.grid(row=0, column=3, rowspan=20, columnspan=5)
    # list.bind("<<ListboxSelection>>",)


def scrollbar(win):
    sb = Scrollbar(win)
    sb.grid(row=1, column=10, rowspan=20)


def buttons(win):
    add_button = Button(win, text="Add", width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    add_button.grid(row=4, column=0)

    search_button = Button(win, text="Search", width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    search_button.grid(row=4, column=1)

    delete_button = Button(win, text="Delete", width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    delete_button.grid(row=6, column=0)

    viewAll_button = Button(win, text="View All", width=12, pady=5, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    viewAll_button.grid(row=6, column=1)

    close_button = Button(win, text="Close", width=12, pady=5, command=win.destroy, border=5, activeforeground="#d6d0d0", activebackground="#f5f2f2", bg="#292525", fg="#d6d0d0")
    close_button.place(x=100, y=170)


def main():
    win = Tk()
    win.geometry("635x245")
    win.title("Book Keeper")
    win['bg'] = "#0f0f0f"

    label(win)
    entry(win)
    list_box(win)
    scrollbar(win)
    buttons(win)

    win.mainloop()


if __name__ == '__main__':
    main()
