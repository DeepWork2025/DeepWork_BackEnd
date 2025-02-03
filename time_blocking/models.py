from django.db import models

# Create your models here.
import pymysql
import pymysql.cursors

# 连接MySQL的特定数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Pass1234', charset='utf8', db='deepwork_v1')
# 收发数据的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)