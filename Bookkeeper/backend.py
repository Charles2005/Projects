import sqlite3


def connect():
    conn = sqlite3.connect("finish.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS finish (Id INTEGER PRIMARY KEY, book text, author text, date text)")
    conn.commit()
    conn.close()


def insert(book, author, date):
    conn = sqlite3.connect("finish.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO finish VALUES (NULL, ?, ?, ?)", (book, author, date))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("finish.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM finish")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("finish.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM finish WHERE id=?", (id,))
    conn.commit()
    conn.close()


def search(book="", author="", date=""):
    conn = sqlite3.connect("finish.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM finish WHERE book=? OR author=? OR date=?", (book, author, date))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


connect()


