import datetime
import numpy as np
# import MySQLdb as SQL
import pymysql.cursors

config = {"host": '60.205.94.60',
          "port": 33009,
          "user": 'bluestackscn',
          "password": 'Bluestacks2016',
          "db": 'bs_datastats',
          "charset": 'utf8',
          "cursorclass": pymysql.cursors.DictCursor}

connection = pymysql.connect(**config)

tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=-1)
print(tomorrow)
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'select result_date,install_success_user from stats_emulator where scope_id=1 and result_date >="2017-09-01"'
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
