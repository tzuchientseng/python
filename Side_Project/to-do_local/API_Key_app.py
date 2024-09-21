from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import webbrowser
import os

app = Flask(__name__)
CORS(app)

API_BASE_URL = "https://todo-notes-d24c2cb2c355.herokuapp.com/"
API_KEY = "aaa78239bfae820d86210233ad995d3d408ffda5fd82f892290206ce148f6931"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    headers = {'API-Key': API_KEY}
    try:
        response = requests.get(f"{API_BASE_URL}/tasks", headers=headers)
        response.raise_for_status() 
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # 增加日誌記錄
        return jsonify({"error": str(http_err)}), response.status_code
    except Exception as err:
        print(f"Other error occurred: {err}")  # 增加日誌記錄
        return jsonify({"error": str(err)}), 500

@app.route('/save_tasks', methods=['POST'])
def save_tasks():
    headers = {'API-Key': API_KEY, 'Content-Type': 'application/json'}
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400
    try:
        response = requests.post(f"{API_BASE_URL}/store-data", headers=headers, json=data)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # 增加日誌記錄
        return jsonify({"error": str(http_err)}), response.status_code
    except Exception as err:
        print(f"Other error occurred: {err}")  # 增加日誌記錄
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://127.0.0.1:7777")
    app.run(debug=True, port=7777)
