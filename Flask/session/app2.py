from cs50  import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# sqlite3 froshims.db
""" 
.schema 快速了解資料表的欄位名稱、資料型別以及該表的其他結構定義。
.schema table_name
sqlite3 froshims.db # 開啟命令 sqlite> SELECT * FROM registrants
"""

db = SQL('sqlite:///froshims.db')

REGISTRANTS = {}

SPORTS = ['Basketball', 'Football', 'Soccer', 'Ultimate Frisbee']

@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)

@app.route('/register', methods=['POST'])
def register():
    # Validate name
    name = request.form.get('name')
    if not name:
        return render_template('error.html', message='Missing name')
    
    # Fetch and print sport selections for debugging
    sports_selected = request.form.getlist('sport')
    print(f"Selected sports: {sports_selected}")  # Add this line for debugging

    if not sports_selected:
        return render_template('error.html', message='Missing sport')
    
    # Remember registrant
    db. execute('INSERT INTO registrants (name, sport) VALUES(?,?)', name, sport)

    # Validate each selected sport
    for sport in sports_selected:
        if sport not in SPORTS:
            return render_template('error.html', message='Invalid sport selected')

    # Store the valid name and selected sports
    REGISTRANTS[name] = sports_selected

    return redirect('/registrants')

@app.route('/registrants')
def registrants():
    registrants = db.execute('SELECT * FROM registrants')
    return render_template('registrants.html', registrants=registrants)

@app.route('/deregister', methods=['POST'])
def deregister():
    # Forget registerant
    id = request.form.get('id')
    if id:
        db.execute('DELETE FROM registrants WHERE id = ?', id)
    return redirect('./registrants')

if __name__ == "__main__":
    app.run(debug=True)
