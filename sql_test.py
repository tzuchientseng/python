import mysql.connector
from mysql.connector import Error
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s- %(message)s')

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='open',
            database='test'
        )
        logging.info("Connect successful!")
        return connection
    except Error as e:
        logging.error(f"Connect status: {e}")
        return None

def show_tables(cursor):
    cursor.execute('SHOW TABLES;')
    for table in cursor.fetchall():
        logging.info(table)

def describe_table(cursor, table):
    cursor.execute(f'DESCRIBE {table};')
    columns = cursor.fetchall()
    df = pd.DataFrame(columns, columns=['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'])
    logging.info(f"Description of table {table}:\n{df}")

def select_all(cursor, table):
    try:
        cursor.execute(f'SELECT * FROM {table};')
        records = cursor.fetchall()
        df = pd.DataFrame(records, columns=[desc[0] for desc in cursor.description])
        logging.info(f"Records from {table}:\n{df}")
        return df
    except Error as e:
        logging.error(f"Error fetching data from {table}: {e}")
        return None

def main():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS `test`")
        # cursor.execute("USE `test`")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `employee`(
                `emp_id` INT PRIMARY KEY,
                `name` VARCHAR(20),
                `birth_date` DATE,
                `sex` VARCHAR(1),
                `salary` INT, 
                `branch_id` INT, 
                `sup_id` INT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `branch`(
                `branch_id` INT PRIMARY KEY,
                `branch_name` VARCHAR(20),
                `manage_id` INT,
                FOREIGN KEY (`manage_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL
            );
        """)
        cursor.execute("""
            ALTER TABLE `employee`
            ADD FOREIGN KEY (`branch_id`)
            REFERENCES `branch`(`branch_id`)
            ON DELETE SET NULL;
        """)
        cursor.execute("""
            ALTER TABLE `employee`
            ADD FOREIGN KEY (`sup_id`)
            REFERENCES `employee`(`emp_id`)
            ON DELETE SET NULL;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `client`(
                client_id INT PRIMARY KEY,
                client_name VARCHAR(20),
                phone VARCHAR(20)
            );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `works_with`(
            emp_id INT,
            client_id INT,
            total_sales INT,
            PRIMARY KEY (`emp_id`, `client_id`),
            FOREIGN KEY (`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
            FOREIGN KEY (`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
            );
        """)

        cursor.execute("INSERT IGNORE INTO `branch` VALUES(1, '研發', NULL);")
        cursor.execute("INSERT IGNORE INTO `branch` VALUES(2, '行政', NULL);")
        cursor.execute("INSERT IGNORE INTO `branch` VALUES(3, '資訊', NULL);")
        cursor.execute("INSERT IGNORE INTO `branch` VALUES(4, '偷懶', NULL);")
        cursor.execute("INSERT IGNORE INTO `employee` VALUES(206, '小黃', '1998-10-08', 'F', 50000, 1, NULL);")
        cursor.execute("INSERT IGNORE INTO `employee` VALUES(207, '小綠', '1985-09-16', 'M', 29000, 2, 206);")
        cursor.execute("INSERT IGNORE INTO `employee` VALUES(208, '小黑', '2000-12-19', 'M', 35000, 3, 206);")
        cursor.execute("INSERT IGNORE INTO `employee` VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);")
        cursor.execute("INSERT IGNORE INTO `employee` VALUES(210, '小蘭', '1925-11-10', 'F', 84000, 1, 207);")
        cursor.execute("INSERT IGNORE INTO `client` VALUES(400, '阿狗', '254354335');")
        cursor.execute("INSERT IGNORE INTO `client` VALUES(401, '阿貓', '25633899');")
        cursor.execute("INSERT IGNORE INTO `client` VALUES(402, '旺來', '45354345');")
        cursor.execute("INSERT IGNORE INTO `client` VALUES(403, '露西', '54354365');")
        cursor.execute("INSERT IGNORE INTO `client` VALUES(404, '艾瑞克', '18783783');")
        cursor.execute("INSERT IGNORE INTO `works_with` VALUES(206, 400, '70000');")
        cursor.execute("INSERT IGNORE INTO `works_with` VALUES(207, 401, '24000');")
        cursor.execute("INSERT IGNORE INTO `works_with` VALUES(208, 402, '9800');")
        cursor.execute("INSERT IGNORE INTO `works_with` VALUES(208, 403, '24000');")
        cursor.execute("INSERT IGNORE INTO `works_with` VALUES(210, 404, '87940');")

        # show_tables(cursor)
        # describe_table(cursor, 'employee')
        # describe_table(cursor, 'branch')
        # select_all(cursor, 'employee')
        cursor.close()
        connection.commit()
        connection.close()
    else:
        logging.error("Connection Failed!")

if __name__ == '__main__':
    main()

logging.debug(
"""

"""
)
