import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book_info (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("INSERT INTO book_info VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM book_info")
    rows = curr.fetchall()
    conn.close() 
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM book_info WHERE author=? OR title=? OR year=? OR isbn=?", (author, title, year, isbn))
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM book_info where id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("UPDATE book_info SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
# insert("The Sea", "John Tablet", 1918, 1234567890)
# insert("The Sun", "John Moore", 1927, 9683422343)
# insert("The Moon", "Smith Will", 1908, 3423423490)
# print(view())
