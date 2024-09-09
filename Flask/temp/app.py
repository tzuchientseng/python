from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
