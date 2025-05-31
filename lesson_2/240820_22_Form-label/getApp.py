from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form_get.html')

@app.route('/submit', methods=['GET'])
def submit():
    userid = request.args.get('userid')
    username = request.args.get('username')
    userpwd = request.args.get('userpwd')
    phone = request.args.get('phone')
    mynum = request.args.get('mynum')
    usremail = request.args.get('usremail')
    usrcolor = request.args.get('usrcolor')
    mydate = request.args.get('mydate')
    mytime = request.args.get('mytime')
    mydatetime = request.args.get('mydatetime')
    gender = request.args.get('gender')
    info = request.args.getlist('info[]')
    select_one = request.args.get('select_one')
    comment = request.args.get('comment')

    return f"""
    <h1>Form Data Submitted via GET</h1>
    <p>UserID: {userid}</p>
    <p>UserName: {username}</p>
    <p>UserPwd: {userpwd}</p>
    <p>Phone: {phone}</p>
    <p>Quantity: {mynum}</p>
    <p>Email: {usremail}</p>
    <p>Color: {usrcolor}</p>
    <p>Date: {mydate}</p>
    <p>Time: {mytime}</p>
    <p>Datetime: {mydatetime}</p>
    <p>Gender: {gender}</p>
    <p>Info: {info}</p>
    <p>Select One: {select_one}</p>
    <p>Comment: {comment}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
