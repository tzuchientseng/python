from flask import Flask, render_template
from flask_cors import CORS
import webbrowser
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://127.0.0.1:7778")
    app.run(debug=True, port=7778)
