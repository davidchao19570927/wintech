# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/20  8:40 
# 文件名称   ：service.py
# 开发工具   ：PyCharm

import pymysql # 导入操作MySQL数据库的模块
import mysql.connector
userName="" # 记录用户名

# 打开数据库连接
class service(object):
 def open():
    #db = pymysql.connect("localhost", "root", "ab145694", "school",charset="utf8")
    db = mysql.connector.connect(host="localhost",database='school',user="root",password="ab145694")  
# creating database_cursor to perform SQL operation  
    #db_cursor = db_connection.cursor(buffered=True) # "buffered=True".makes db_cursor.row_count return actual number of records selected otherwise would return -1  
    return db # 返回连接对象

# 执行数据库的增、删、改操作
 def exec(sql,values):
    #db=open() # 连接数据库
    #cursor = db.cursor() # 使用cursor()方法获取操作游标
    db = mysql.connector.connect(host="localhost",database='school',user="root",password="ab145694")  
    db_cursor = db.cursor(buffered=True)
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql,values) # 执行增删改的SQL语句
        db.commit() # 提交数据
        return 1 # 执行成功
    except:
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败
    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接

# 带参数的精确查询
 def query(sql,*keys):
   # db=open() # 连接数据库
    db = mysql.connector.connect(host="localhost",database='school',user="root",password="ab145694")  
    db_cursor = db.cursor(buffered=True)
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql,keys) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果

# 不带参数的模糊查询
 def query2(sql):
    #db=open() # 连接数据库
    #cursor = db.cursor() # 使用cursor()方法获取操作游标
    db = mysql.connector.connect(host="localhost",database='school',user="root",password="ab145694")  
    cursor = db.cursor(buffered=True)
    cursor.execute(sql) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果
