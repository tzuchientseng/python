"""
底下是建立資料表的SQL語法

use cloud;
CREATE TABLE `旅遊軌跡` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userId` tinyint NOT NULL,
  `lng` double NOT NULL,
  `lat` double NOT NULL,
  `eventDay` date NOT NULL,
  `eventTime` time NOT NULL,
  `startFlag` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`),
  KEY `eventDay` (`eventDay`),
  KEY `userId` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci
"""
import mysql.connector as mysql
from G import G
conn=mysql.connect(host="mahaljsp.asuscomm.com", user="lcc", password="lcc0507", database="cloud")
cursor=conn.cursor()
cmd="select * from 旅遊軌跡 order by eventDay"
cursor.execute(cmd)
rs=cursor.fetchall()
conn.close()
datas=[]
for r in rs:
    datas.append([r[1], r[2], r[3], r[4], r[5], r[6]])

conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database=G.db)
cursor=conn.cursor()
cmd="insert into 旅遊軌跡 (userId, lng, lat, eventDay, eventTime, startFlag) values (%s, %s, %s, %s, %s, %s)"
cursor.executemany(cmd, datas)
conn.commit()
conn.close()