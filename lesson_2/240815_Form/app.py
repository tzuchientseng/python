from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 從表單中獲取資料
        userid = request.form.get('userid')
        username = request.form.get('username')
        userpwd = request.form.get('userpwd')
        phone = request.form.get('phone')
        mynum = request.form.get('mynum')
        usremail = request.form.get('usremail')
        usrcolor = request.form.get('usrcolor')
        mydate = request.form.get('mydate')
        mytime = request.form.get('mytime')
        mydatetime = request.form.get('mydatetime')
        gender = request.form.get('gender')
        info = request.form.getlist('info[]')
        select_one = request.form.get('select_one')
        comment = request.form.get('comment')

        # 處理文件上傳
        mypic = request.files.get('mypic')
        myfiles = request.files.getlist('myfile[]')

        # 這裡可以處理表單數據，例如儲存到資料庫，或是做其他邏輯處理

        # 顯示獲取到的表單資料
        print(f"UserID: {userid}")
        print(f"UserName: {username}")
        print(f"UserPwd: {userpwd}")
        print(f"Phone: {phone}")
        print(f"Quantity: {mynum}")
        print(f"Email: {usremail}")
        print(f"Color: {usrcolor}")
        print(f"Date: {mydate}")
        print(f"Time: {mytime}")
        print(f"Datetime: {mydatetime}")
        print(f"Gender: {gender}")
        print(f"Info: {info}")
        print(f"Select One: {select_one}")
        print(f"Comment: {comment}")

        # 處理上傳的檔案
        if mypic:
            mypic.save(f"./uploads/{mypic.filename}")
            print(f"Saved picture: {mypic.filename}")

        for file in myfiles:
            if file:
                file.save(f"./uploads/{file.filename}")
                print(f"Saved file: {file.filename}")

        return redirect(url_for('index'))  # 提交後重導向首頁

    return render_template('form.html')  # 渲染表單頁面

if __name__ == '__main__':
    app.run(debug=True)
