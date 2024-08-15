from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用 CORS 支持
# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}}) #指定來源

# 模擬資料庫
seats = {}
seating_charts = {}  # 存放座位表的字典

# 獲取所有座位
@app.route('/api/seats', methods=['GET'])
def get_seats():
    return jsonify(list(seats.values()))

# 創建新座位
@app.route('/api/seats', methods=['POST'])
def create_seat():
    data = request.json
    seat_id = data['seat_id']
    position_x = data['position_x']
    position_y = data['position_y']
    seats[seat_id] = {'seat_id': seat_id, 'position_x': position_x, 'position_y': position_y}
    return jsonify(seats[seat_id]), 201

# 更新座位位置
@app.route('/api/seats/<int:seat_id>', methods=['PUT'])
def update_seat(seat_id):
    if seat_id in seats:
        data = request.json
        seats[seat_id]['position_x'] = data['position_x']
        seats[seat_id]['position_y'] = data['position_y']
        return jsonify(seats[seat_id])
    else:
        return jsonify({'error': 'Seat not found'}), 404

# 重置所有座位
@app.route('/api/seats', methods=['DELETE'])
def reset_seats():
    seats.clear()
    return jsonify({'status': 'All seats reset'}), 200

# 保存座位表
@app.route('/api/seating-charts', methods=['POST'])
def save_seating_chart():
    data = request.json
    chart_name = data['name']
    chart_data = data['seats']
    seating_charts[chart_name] = chart_data
    return jsonify({'status': 'Seating chart saved'}), 201

# 獲取所有座位表歷史紀錄
@app.route('/api/seating-charts', methods=['GET'])
def get_seating_charts():
    return jsonify(list(seating_charts.keys()))

# 獲取指定名稱的座位表
@app.route('/api/seating-charts/<chart_name>', methods=['GET'])
def get_seating_chart(chart_name):
    if chart_name in seating_charts:
        return jsonify(seating_charts[chart_name])
    else:
        return jsonify({'error': 'Seating chart not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)


