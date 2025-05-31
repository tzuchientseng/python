import mysql.connector
from mysql.connector import Error
from scraper import all_data
import logging

# logging.basicConfig(level=logging.INFO,
logging.basicConfig(level=logging.CRITICAL,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='open',
            database='NBA' #就不用多寫 USE `NBA
        )
        logging.info("資料庫連接成功")
        return connection
    except Error as e:
        logging.error(f"資料庫連接錯誤: {e}")
        return None

def create_database_and_table(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS `NBA`;")
        cursor.execute("USE `NBA`;")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Regular_Season` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Player_Name VARCHAR(50),
            Season VARCHAR(10),
            Age INT,
            Tm VARCHAR(10),
            Lg VARCHAR(10),
            Pos VARCHAR(5),
            G INT,
            GS INT,
            MP FLOAT,
            FG FLOAT,
            FGA FLOAT,
            FG_Percentage FLOAT,
            `3P` FLOAT,
            `3PA` FLOAT,
            `3P_Percentage` FLOAT,
            `2P` FLOAT,
            `2PA` FLOAT,
            `2P_Percentage` FLOAT,
            eFG_Percentage FLOAT,
            FT FLOAT,
            FTA FLOAT,
            FT_Percentage FLOAT,
            ORB FLOAT,
            DRB FLOAT,
            TRB FLOAT,
            AST FLOAT,
            STL FLOAT,
            BLK FLOAT,
            TOV FLOAT,
            PF FLOAT,
            PTS FLOAT,
            UNIQUE KEY `player_season` (Player_Name, Season)
        );
        """)
        logging.info("表格創建完成或已存在")
    except Error as e:
        logging.error(f"創建資料庫或表格時出錯: {e}")

def clean_and_convert(value):
    if value == '' or value == 'None':
        return None
    try:
        return float(value)
    except ValueError:
        return value

def insert_data(cursor, connection):
    insert_query = """
    INSERT IGNORE INTO `Regular_Season` (
        Player_Name, Season, Age, Tm, Lg, Pos, G, GS, MP, FG, FGA, FG_Percentage, 
        `3P`, `3PA`, `3P_Percentage`, `2P`, `2PA`, `2P_Percentage`, 
        eFG_Percentage, FT, FTA, FT_Percentage, ORB, DRB, TRB, AST, STL, 
        BLK, TOV, PF, PTS
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    error_records = []
    inserted_count = 0
    
    for player, records in all_data.items():
        for record in records[1:]:  # 跳過標題行
            try:
                processed_record = [player] + [clean_and_convert(value) for value in record[:-1]]  # 排除最後一個欄位（獎項）
                
                if len(processed_record) != 31:  # 30個欄位 + player_name
                    if "Did Not Play" in record[1]:  # 處理特殊情況
                        continue  # 跳過這個記錄
                    else:
                        logging.warning(f"跳過記錄,欄位數不正確: {player}, {record[0]}")
                        error_records.append((player, record))
                        continue
                
                cursor.execute(insert_query, tuple(processed_record))
                if cursor.rowcount > 0:
                    inserted_count += 1
            except Error as e:
                logging.error(f"插入記錄時出錯 {player}, {record[0]}: {e}")
                error_records.append((player, record))
    
    connection.commit()
    logging.info(f"資料插入完成，新增了 {inserted_count} 條記錄")
    
    return error_records

def main():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        create_database_and_table(cursor)
        
        error_records = insert_data(cursor, connection)
        
        if error_records:
            logging.warning("以下記錄插入失敗:")
            for player, record in error_records:
                logging.warning(f"{player}: {record}")
        
        cursor.execute("SELECT COUNT(*) FROM Regular_Season;")
        row_count = cursor.fetchone()
        logging.info(f"Regular_Season 表格中的資料總筆數: {row_count[0]}")
        
        cursor.close()
        connection.close()
    else:
        logging.error("無法建立資料庫連接")

if __name__ == "__main__":
    main()
