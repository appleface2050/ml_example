import datetime
import seaborn as sns
import numpy as np
import pandas as pd
# import MySQLdb as SQL
import pymysql.cursors
import matplotlib.pyplot as plt

con = {"host": '60.205.94.60',
       "port": 33009,
       "user": 'bluestackscn',
       "password": 'Bluestacks2016',
       "db": 'bs_datastats',
       "charset": 'utf8',
       "cursorclass": pymysql.cursors.DictCursor}

connection = pymysql.connect(**con)

con_monitor = {"host": '60.205.94.60',
               "port": 33006,
               "user": 'bluestackscn',
               "password": 'Bluestacks2016',
               "db": 'bst-monitor',
               "charset": 'utf8',
               "cursorclass": pymysql.cursors.DictCursor}
connection_monitor = pymysql.connect(**con_monitor)

def get_whole_day_result_by_date_range(dt_start, dt_end):
    data = []
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = """
            SELECT result_date, install_success_user FROM stats_emulator
            WHERE result_date >="%s" and result_date <"%s"
            AND scope_id = 1
            """ % (dt_start, dt_end)
            # print (sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                data.append(i["install_success_user"])
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        pass
    return data


def get_monitor_data_by_date_range_and_hour(hour, dt_start, dt_end):
    data = []
    try:
        with connection_monitor.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = """
          SELECT result_date, HOUR, install_success_user FROM monitor_odps_emulatormonitorstats
          WHERE result_date >="%s" AND result_date< "%s" AND HOUR = "%s"
          ORDER BY result_date asc
            """ % (dt_start, dt_end, hour)
            # print (sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                data.append(i["install_success_user"])
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        pass
    return data


dt_list = []
init_monitor_dict = {}

try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql_date = 'select DISTINCT DATE_FORMAT(result_date, "%Y-%m-%d") as dt from stats_emulator where scope_id=1 and result_date >="2017-09-01" and result_date < "2017-09-30"'
        cursor.execute(sql_date)
        result = cursor.fetchall()
        for i in result:
            # print(i)
            dt_list.append(i["dt"])
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    pass

# print (dt_list)
init_monitor_dict["date"] = dt_list

for hour in ["00", "01", "02", "03", "04", "05", "06", "07", "08"]:
    init_monitor_dict[hour] = get_monitor_data_by_date_range_and_hour(hour, "2017-09-01", "2017-09-30")

init_monitor_dict["y"] = get_whole_day_result_by_date_range("2017-09-01", "2017-09-30")


# print (init_monitor_dict)

df_monitor = pd.DataFrame(init_monitor_dict)
print(df_monitor)
print (df_monitor.info())

connection.close()
connection_monitor.close()

# df_show = pd.DataFrame({"x":df_monitor["05"], "y":df_monitor["y"]})

# sns.lmplot("01","y", df_monitor)
# # plt.plot(df_monitor["00"], df_monitor["y"])
# plt.show()

