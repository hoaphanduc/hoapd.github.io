import sqlite3

connection = sqlite3.connect('bookdata.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO author (authorid,name,priority) VALUES (?,?,?)",
            ('1','Nguyen Du','nope')
            )
cur.execute("INSERT INTO author (authorid,name,priority) VALUES (?,?,?)",
            ('2','To Huu','nope')
            )
cur.execute("INSERT INTO book (bookid, title,authorid) VALUES (?,?,?)",
            ('1', 'Truyen Kieu','1')
            )
cur.execute("INSERT INTO book (bookid, title,authorid) VALUES (?,?,?)",
            ('2', 'Tu Ay','2')
            )
cur.execute("INSERT INTO users (user, pass) VALUES (?,?)",
            ('hoapd','pdhoa')
            )
connection.commit()
connection.close()