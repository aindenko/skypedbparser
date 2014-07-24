__author__ = 'andrey'
import sqlite3
import settings
import configparser
import logging

logging.basicConfig(filename='my.log',filemode='w',level=logging.DEBUG)

logging.debug('Parser started');


from os.path import expanduser
home = expanduser("~")
logging.debug('Home dir is '+home);


#connect db
conn = sqlite3.connect(settings.path + '/main.db')
#sql
sql = "SELECT Chats.activity_timestamp FROM Chats WHERE name=? ORDER by id desc "
logging.debug(sql)
#execute
res = conn.execute(sql,[settings.chat])
res.fetchall()


sql = "SELECT * FROM Messages WHERE chatname='"+settings.chat+"' ORDER by id desc LIMIT 20"
logging.debug(sql)
#execute
res = conn.execute(sql)
res.fetchall()


#config load
config = configparser.RawConfigParser()
config.read('my.ini')

path = config.get('system', 'path')
chat = config.get('system', 'chat')

#config.add_section('system')
my = config.set('system', 'my',3)


#config save
with open('my.ini', 'w') as configfile:
    config.write(configfile)
