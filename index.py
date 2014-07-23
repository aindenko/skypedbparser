__author__ = 'andrey'
import sqlite3
import settings


print("Hello World!")

from os.path import expanduser
home = expanduser("~")

#connect db
conn = sqlite3.connect(settings.path + '/main.db')
#sql
sql = "SELECT Chats.activity_timestamp FROM Chats WHERE name='"+settings.chat+"' ORDER by id desc "

#execute
res = conn.execute(sql)
print(res.fetchall())


sql = "SELECT * FROM Messages WHERE chatname='"+settings.chat+"' ORDER by id desc LIMIT 20"

#execute
res = conn.execute(sql)
print(res.fetchall())
print(home)
