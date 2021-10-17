import pymysql.cursors
connection = pymysql.connect(host="192.168.75.143",
                             port=3306,
                             user="root",
                             password="ly86036609",
                             db='DouBanTop250',
                             charset="utf8",
                             )

# try:
cursor = connection.cursor()
# sql = "INTERT INTO Text1(link,imglink,point,pointer,info,CnName,OutName) VALUES('1','2','3','4','5','6','7');"
# sql = "CREATE TABLE t1(id int not null,name char(20));"
sql = "INSERT INTO t1(`id`)VALUES('4');"
cursor.execute(sql)
# result = cursor.fetchall()
# sql = "select * from t1;"
# cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()