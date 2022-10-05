import sqlite3


def connect():
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    con.commit()
    con.close()


def drop_table():
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS book')
    con.commit()
    con.close()


def insert(title, author, year, isbn):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute('INSERT INTO book VALUES(NULL, ?,?,?,?)', (title, author, year, isbn))
    con.commit()
    con.close()


def view_all():
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    con.close()
    return rows


def search(title='', author='', year='', isbn=''):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows


def delete(id=None, title='', author='', year='', isbn=''):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute('DELETE FROM book WHERE id=? OR title=? OR author=? OR year=? OR isbn=?',
                (id, title, author, year, isbn))
    con.commit()
    con.close()


def update(id, title, author, year, isbn):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?',
                (title, author, year, isbn, id))
    con.commit()
    con.close()


connect()
#update(2, 'The Terra', 'Mooner Smoother', 2011, 20110001)
print(view_all())

#insert('The moon', 'Many the Fanny', 1932, 19320001)
#delete(id=3)
#print(search(author='John Tablet'))