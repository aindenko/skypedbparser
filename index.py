__author__ = 'andrey'
import sqlite3
import settings


print("Hello World!")

#connect db
conn = sqlite3.connect(settings.path + '/main.db')
#sql
sql = "SELECT * FROM Chats LIMIT 10"

#execute
res = conn.execute(sql)
print(res.fetchall())
