import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
import webbrowser
import os

# 設定日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 建立 Flask 應用
app = Flask(__name__)
CORS(app)

# 創建 MySQL 連接
def create_connection(db_name=None):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='open',  
            database=db_name if db_name else None  # 根據需要選擇是否指定資料庫
        )
        logging.info(f"資料庫{'連接到 ' + db_name if db_name else '連接成功'}")
        return connection
    except Error as e:
        logging.error(f"資料庫連接錯誤: {e}")
        return None

def create_database_and_table():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS `todo_app`;")
            logging.info("資料庫 `todo_app` 創建完成或已存在")
            cursor.execute("USE `todo_app`;")
            logging.info("成功切換至資料庫 `todo_app`")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS `tasks` (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task_text VARCHAR(255) NOT NULL,
                status ENUM('todo', 'completed') NOT NULL
            );
            """)
            logging.info("表格 `tasks` 創建完成或已存在")
        except Error as e:
            logging.error(f"創建資料庫或表格時出錯: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        logging.error("無法連接到 MySQL，資料庫和表格創建失敗")

# 插入數據
def insert_tasks(cursor, connection, todos, completed):
    try:
        insert_query = """
        INSERT INTO `tasks` (task_text, status) VALUES (%s, %s);
        """
        
        # 清空原有數據
        cursor.execute("DELETE FROM tasks")

        # 插入新的待辦事項
        for task in todos:
            cursor.execute(insert_query, (task, 'todo'))

        # 插入新的已完成事項
        for task in completed:
            cursor.execute(insert_query, (task, 'completed'))

        connection.commit()
        logging.info("資料插入完成")
    except Error as e:
        logging.error(f"插入資料時出錯: {e}")

# 根路由，返回index.html
@app.route('/')
def index():
    return render_template('index.html')

# Flask 路由來保存待辦事項
@app.route('/save-tasks', methods=['POST'])
def save_tasks():
    create_database_and_table()  # 確保資料庫和表格已存在
    connection = create_connection('todo_app')
    if connection is not None:
        cursor = connection.cursor()
        
        data = request.json
        todos = data.get('todos')
        completed = data.get('completed')
        
        insert_tasks(cursor, connection, todos, completed)
        
        cursor.close()
        connection.close()
        
        return jsonify({'message': 'Tasks saved successfully!'}), 200
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    create_database_and_table()  # 確保資料庫和表格已存在
    connection = create_connection('todo_app')
    if connection is not None:
        try:
            cursor = connection.cursor()
            logging.info("Successfully connected to the database and obtained cursor.")
            cursor.execute("SELECT task_text, status FROM tasks")
            tasks = cursor.fetchall()
            logging.info(f"Fetched tasks: {tasks}")
            
            todos = [task[0] for task in tasks if task[1] == 'todo']
            completed = [task[0] for task in tasks if task[1] == 'completed']

            return jsonify({'todos': todos, 'completed': completed}), 200
        except Error as e:
            logging.error(f"Error during fetching tasks: {e}")
            return jsonify({'error': 'Failed to fetch tasks from database'}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

@app.route('/clear-tasks', methods=['POST'])
def clear_tasks():
    connection = create_connection('todo_app')
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS tasks;")
            connection.commit()
            logging.info("表格 `tasks` 已被刪除")
            return jsonify({'message': 'Tasks table cleared successfully!'}), 200
        except Error as e:
            logging.error(f"刪除表格時出錯: {e}")
            return jsonify({'error': 'Failed to clear tasks'}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

# if __name__ == '__main__':
    # app.run(debug=True)

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://127.0.0.1:5000") #瀏覽器運行
    app.run(debug=True)
