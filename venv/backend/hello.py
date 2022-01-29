from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import send_file
from sqlalchemy import null

app = Flask(__name__)

@app.route('/')
def hello():
  return "<p>Hello, World!</p>"

@app.route('/<name>')
def hello_name(name):
  return f"<p>Hello, {escape(name)}!</p>"

@app.route('/games')
def games():
  return f"My favorite games are World of Warcraft, Counter Strike and Call of Duty"


@app.route('/error')
def error():
  return send_file('../static/error.gif')






@app.route('/courses', methods=['GET'])
def courses():
  return f"Here will be courses displayed"


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if (
      request.form['username']!=null &
      request.form['password']!=null
    ):
      return send_file('../static/loginsuccessful.gif')
    else: 
      return f'do_the_login()'
  else: 
    return send_file('../static/login.gif')

@app.route('/users', methods=['GET'])
def users():
  return f"Here will be all USERS displayed"

@app.route('/user/<username>', methods=['GET'])
def user(username):
  return f"Here will be the user with the {escape(username)} displayed"

@app.route('/user/<int:userid>', methods=['GET'])
def user_by_id(userid):
  return f"Here will be the user with the {escape(userid)} displayed"


@app.route('/lectures', methods=['GET'])
def lectures():
  return f"Here will be LECTURES displayed"


@app.route('/emotions', methods=['GET'])
def emotions():
  return f"Here will be EMOTIONS displayed"


