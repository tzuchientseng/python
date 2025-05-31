from flask import Flask, render_template, request, redirect, session
from cs50 import SQL

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

REGISTRANTS = {}

db = SQL('sqlite:///show.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q')
    shows = db.execute('SELECT * FROM shows WHERE title LIKE ?', '%' + q + '%')
    return render_template('search.html', shows=shows)

@app.route('/register', methods=['POST'])
def register():
    # Validate name
    name = request.form.get('name')
    if not name:
        return render_template('error.html', message='Missing name')
    
    # Fetch and print sport selections for debugging
    sports_selected = request.form.getlist('sport')
    print(f"Selected sports: {sports_selected}")  # Debugging line

    if not sports_selected:
        return render_template('error.html', message='Missing sport')
    
    # Validate each selected sport
    for sport in sports_selected:
        if sport not in SPORTS:
            return render_template('error.html', message='Invalid sport selected')

    # Store the valid name and selected sports
    REGISTRANTS[name] = sports_selected

    return redirect('/registrants')

@app.route('/registrants')
def registrants():
    return render_template('registrants.html', registrants=REGISTRANTS)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    # Ensure cart exists
    if 'cart' not in session:
        session['cart'] = []

    # POST
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")

    # GET
    cart_ids = session.get('cart', [])
    if not cart_ids:
        books = []
    else:
        # Adjust SQL query to handle a list of IDs
        books = db.execute("SELECT * FROM books WHERE id IN (" + ",".join("?" * len(cart_ids)) + ")", *cart_ids)
    return render_template("cart.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
