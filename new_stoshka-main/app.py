from flask import Flask, render_template
# from sql import

app = Flask(__name__, static_folder='css')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/course.html')
def course():
    return render_template('course.html')
app.run()