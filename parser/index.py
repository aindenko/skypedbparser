__author__ = 'andrey'
import sqlite3
import configparser
import logging
import os
os.chdir(os.path.dirname(__file__))
print(os.getcwd())


cfgfile = 'my.ini'
#config load
config = configparser.RawConfigParser()
config.read(cfgfile)

#get params
path = config.get('system', 'path')
chat = config.get('system', 'chat')
ts = config.getint('system', 'ts')
msgid = config.getint('system', 'msgid')

logging.basicConfig(filename='my.log',filemode='a',level=logging.DEBUG)
logging.debug('///////////////////////////////////////////////');
logging.debug('Parser started');


#connect db
conn = sqlite3.connect(path + '/main.db')
#sql check last activity ts
sql = "SELECT Chats.activity_timestamp FROM Chats WHERE name=? ORDER by id desc "
logging.debug(sql)
#execute
res = conn.execute(sql,[chat])
lastactts = res.fetchall()[0][0]
# check that ts was changes
if lastactts > ts :
    sql = "SELECT * FROM Messages WHERE chatname = ? AND id > ? ORDER by id desc LIMIT 20"
    logging.debug(sql)
    #execute
    res = conn.execute(sql,[chat,msgid])
    msgs = res.fetchall()
    logging.debug(msgs)
    #set last message id
    config.set('system', 'msgid',msgs[0][0])
    config.set('system', 'ts', lastactts)

    #config save
    with open(cfgfile, 'w') as configfile:
        config.write(configfile)
