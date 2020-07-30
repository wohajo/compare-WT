from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp_db.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/compare-planes')
def compare_planes():
    return render_template('planes.html', title='Compare planes')

@app.route('/compare-tanks')
def compare_tanks():
    return render_template('tanks.html', title='Compare tanks')

@app.route('/compare-helicopters')
def compare_helicopters():
    return render_template('helicopters.html', title='Compare helicopters')

@app.route('/compare-fleet')
def compare_fleet():
    return render_template('fleet.html', title='Compare fleet')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
