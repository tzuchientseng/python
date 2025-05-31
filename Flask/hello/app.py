from flask import Flask, render_template, request

# 建立 Flask 應用程式實例
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name') 
        return render_template('greet.html', name=name)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
  