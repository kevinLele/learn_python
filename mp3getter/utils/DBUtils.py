# coding:utf-8

import sqlite3

conn = None


# 初始化数据库连接
def init_connection(db_path):
    global conn
    conn = sqlite3.connect(db_path)


def commit():
    if conn is not None:
        conn.commit()


# 关闭数据库连接
def close_connection():
    if conn is not None:
        conn.close()


# 执行SQL更新
def execute_sql(sql, params=()):
    if conn is not None:
        conn.execute(sql, params)
        conn.commit()
    else:
        raise Exception(u'数据库连接未初始化，请先执行init_connection进行初始化')


def search(sql, params=()):
    if conn is not None:
        return conn.execute(sql, params)
    else:
        raise Exception(u'数据库连接未初始化，请先执行init_connection进行初始化')

if __name__ == "__main__":
    init_connection("../../test.db")
    execute_sql("insert into story (sn,id,name,path) values (?,?,?,?)", (1, 2, 3, 4))

