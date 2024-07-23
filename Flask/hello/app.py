from flask import Flask, render_template, request #主要import這三個

# 建立 Flask 應用程式實例
app = Flask(__name__)

# 設定路由和視圖函數
@app.route("/")
def index():
    return render_template("index.html")   #conventional 寫法 寫成為依樣

@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
