import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT id FROM Genre WHERE name = ? ', ("adad", ))

row = cur.fetchone()
print row