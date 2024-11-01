'''
底下是資料表
use cloud;
CREATE TABLE `旅遊案件` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` tinyint NOT NULL,
  `lng` double NOT NULL,
  `lat` double NOT NULL,
  `area` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `address` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `eventDay` date NOT NULL,
  `eventTime` time NOT NULL,
  `damageType` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `photo` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `patrolNo` varchar(13) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `eventDay` (`eventDay`),
  KEY `area` (`area`),
  KEY `damageType` (`damageType`),
  KEY `userId` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci
'''
from G import G
import mysql.connector as mysql
conn=mysql.connect(host="mahaljsp.asuscomm.com", user="lcc", password="lcc0507", database="cloud")
cursor=conn.cursor()
cmd="select * from 旅遊案件 where eventDay >='2023-10-01'"
cursor.execute(cmd)
rs=cursor.fetchall()
datas=[]
for r in rs:
    datas.append([r[1],r[2],r[3],r[4],r[5],r[6],r[7], r[8], r[9]])
cursor.close()
conn.close()

conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database="cloud")
cursor=conn.cursor()
cmd="insert into 旅遊案件 (userId, lng, lat, area, address, eventDay, eventTime, damageType, photo) values (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
cursor.executemany(cmd, datas)
conn.commit()
cursor.close()
conn.close()
