from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
app = Flask(__name__)
@app.route('/contact')
def contact () : 
    return render_template('contact.html')
@app.route('/submit', methods = ['POST'])
def submit () :
    name = request.form.get('name')
    email = request.form.get('email')
    return f'thank you, {name} youre email address is {email}.'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.name}>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
if __name__ == "__main__":
     app.run(debug=True)