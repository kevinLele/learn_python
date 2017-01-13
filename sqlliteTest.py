# coding:utf-8

import time
import re
import sys
import os
import requests
from bs4 import BeautifulSoup
import json
import sqlite3

reload(sys)
sys.setdefaultencoding("utf-8")
time.sleep(1)

con = sqlite3.connect("./test.db")
cu = con.cursor()
#cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")

for t in[(0, 10, 'abc', 'Yu'), (1, 20, 'cba', 'Xu')]:
    cu.execute("insert into catalog values (?,?,?,?)", t)

con.commit()
con.close()



