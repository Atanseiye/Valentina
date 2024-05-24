from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy.orm import Mapped, mapped_column
import traceback

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///valentina_new_student.db'
db = SQLAlchemy(app)
# db.init_app(app)


# Create a model for users registration
class registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(80), unique=False, nullable=False)
    l_name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    parent_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"Surname: {self.f_name}, Last Name: {self.l_name}, Address: {self.address}, Parent Name: {self.parent_name}, Email: {self.email}, Phone: {self.phone}"
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/join', methods=['POST', 'GET'])
def join():
    if request.method == 'POST':
        # let's create a model for the request above 
        new_registration = registration(
            f_name = request.form.get('f_name'),
            l_name = request.form.get('l_name'),
            address = request.form.get('address'),
            parent_name = request.form.get('parent_name'),
            email = request.form.get('email'),
            phone = request.form.get('phone'),
        )

        print('Printing new application here:', new_registration)
        # now push it to the database
        try:
            db.session.add(new_registration)
            db.session.commit()
            return redirect('/join') 
        except Exception as e:
            db.session.rollback()  # Roll back the session to clean up the failed transaction
            print('Error details:', str(e))
            print(traceback.format_exc())  # Print the stack trace for more details
            return 'Issues creating registration'

    else:
        return render_template('form.html')


@app.route('/show')
def show():
    applications = registration.query.all()
    return render_template('show.html', applications=applications)
    
