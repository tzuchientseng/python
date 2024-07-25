import mysql.connector

# 建立資料庫連接
connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='open'
)

cursor = connection.cursor()

# 創建資料庫
cursor.execute("CREATE DATABASE IF NOT EXISTS `NBA`;")
cursor.execute("USE `NBA`;")

# 創建表格
cursor.execute("""
CREATE TABLE IF NOT EXISTS `player` (
    `player_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30)
);
""")

# 插入資料
cursor.execute("""
INSERT INTO `player` (`player_id`, `name`)
SELECT 1, 'LeBron James'
FROM DUAL -- (虛擬表)確保返回一行 -- 後面要加一個空白
WHERE NOT EXISTS (
    SELECT 1
    FROM `player`
    WHERE `player_id` = 1
      AND `name` = 'LeBron James'
);
""")

cursor.execute("""
INSERT INTO `player` (`player_id`, `name`)
SELECT 2, 'Stephen Curry'
FROM DUAL
WHERE NOT EXISTS (
    SELECT 1
    FROM `player`
    WHERE `player_id` = 2
      AND `name` = 'Stephen Curry'
);
""")

# 查看表結構
"""
cursor.execute("DESCRIBE `player`;")
records = cursor.fetchall()

# 打印出表結構
print("Table Structure:")
for record in records:
    print(record)
print()
"""

# 查詢所有資料
cursor.execute("SELECT * FROM `player`;")
records = cursor.fetchall()

# 打印出所有資料
print("Data:")
for record in records:
    print(record)

# 提交所有變更
connection.commit()

# 關閉游標和連接
cursor.close()
connection.close()
