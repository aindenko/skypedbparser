__author__ = 'andrey'
import sqlite3
import configparser
import logging

cfgfile = 'my.ini'
#config load
config = configparser.RawConfigParser()
config.read(cfgfile)

path = config.get('system', 'path')
chat = config.get('system', 'chat')
ts = config.get('system', 'ts')

#store last ts
#config.set('system', 'ts',lastts)


logging.basicConfig(filename='my.log',filemode='a',level=logging.DEBUG)
logging.debug('///////////////////////////////////////////////');
logging.debug('Parser started');


from os.path import expanduser
home = expanduser("~")
logging.debug('Home dir is '+home);


#connect db
conn = sqlite3.connect(path + '/main.db')
#sql check last activity ts
sql = "SELECT Chats.activity_timestamp FROM Chats WHERE name=? ORDER by id desc "
logging.debug(sql)
#execute
res = conn.execute(sql,[chat])
lastactts = res.fetchall()[0][0]

if lastactts > ts :
    sql = "SELECT * FROM Messages WHERE chatname= ? ORDER by id desc LIMIT 20"
    logging.debug(sql)
    #execute
    res = conn.execute(sql,[chat])
    logging.debug(res.fetchall())





#config save
with open('my.ini', 'w') as configfile:
    config.write(configfile)
