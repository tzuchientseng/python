from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
import json
import os

# 設定日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 建立 Flask 應用
app = Flask(__name__)
CORS(app)

# JSON 文件路徑
DATA_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

# 根路由，返回index.html
@app.route('/')
def index():
    return render_template('index.html')

# 獲取待辦事項
@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    username = request.args.get('username')
    tasks = load_tasks()
    user_tasks = tasks.get(username, {'todos': [], 'completed': []})
    return jsonify(user_tasks), 200

# 保存待辦事項
@app.route('/save-tasks', methods=['POST'])
def save_tasks_route():
    data = request.json
    username = data.get('username')
    tasks = load_tasks()
    tasks[username] = {
        'todos': data.get('todos', []),
        'completed': data.get('completed', [])
    }
    save_tasks(tasks)
    return jsonify({'message': 'Tasks saved successfully!'}), 200

# 清除所有待辦事項
@app.route('/clear-tasks', methods=['POST'])
def clear_tasks():
    data = request.json
    username = data.get('username')
    tasks = load_tasks()
    if username in tasks:
        tasks[username] = {'todos': [], 'completed': []}
    save_tasks(tasks)
    return jsonify({'message': 'Tasks cleared successfully!'}), 200

# 刪除所有 JSON 資料
@app.route('/drop-json', methods=['POST'])
def drop_json():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)  # 刪除 JSON 文件
        return jsonify({'message': 'All JSON data has been dropped successfully!'}), 200
    else:
        return jsonify({'message': 'No JSON data found to delete.'}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


