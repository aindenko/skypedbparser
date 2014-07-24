__author__ = 'andrey'
import sqlite3
import settings
import configparser
import logging



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


config = configparser.RawConfigParser()
config.read('my.ini')

path = config.get('system', 'path')
chat = config.get('system', 'chat')

#config.add_section('system')
my = config.set('system', 'my',3)

print(path)
with open('my.ini', 'w') as configfile:
    config.write(configfile)
