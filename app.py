from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def abou():
    return render_template('about.html')

@app.route('/courses')
def course():
    return render_template('courses.html')

@app.route('/team')
def tea():
    return render_template('team.html')


@app.route('/testimonial')
def testimonia():
    return render_template('testimonial.html')

@app.route('/contact')
def contac():
    return render_template('contact.html')



