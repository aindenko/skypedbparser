__author__ = 'andrey'
import sqlite3

print("Hello World!")

#connect db
conn = sqlite3.connect('main.db')
#sql
sql = "SELECT * FROM Chats LIMIT 10"

#execute
res = conn.execute(sql)
print(res.fetchall())
