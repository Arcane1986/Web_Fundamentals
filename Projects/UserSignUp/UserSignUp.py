from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
  return render_template('inputs.html', errors = None, username = "", email = "")

@app.route('/add', methods=["GET","POST"])
def add_user():
  error_dict = validater(request.form)
  username = request.form['user-name']
  email = request.form['e-mail']
  if error_dict:
    return render_template("inputs.html", errors = error_dict, username = username, email = email)
    # return render_template('inputs.html', error1 = error_dict['error1'], error2 = error_dict['error2'], error3 = error_dict['error3'], error4 = error_dict['error4'], error5 = error_dict['error5'], error6 = error_dict['error6'], error7 = error_dict['error7'])
  return render_template('welcome.html', username = username)

def validater(form):
  username = form['user-name']
  password = form['p-word']
  verified_password = form['verified-password']
  email = form['e-mail']
  error_dict = {}

  if username == "" or password == "" or verified_password == "" or email =="":
    error_dict['error1'] = "Fill out all fields in order to proceed."
  if len(username) < 3 or len(username) >= 20:
    error_dict['error2'] = "The username cannot be shorter than 3 charters or longer than 20 characters."
  if len(password) < 3 or len(password) >= 20:
    error_dict['error3'] = "The password cannot be shorter than 3 charters or longer than 20 characters."
  if " " in username:
    error_dict['error4'] = "Spaces can not be used in the username."
  if " " in password:
    error_dict['error5'] = "Spaces can not be used in the password."
  if password != verified_password:
    error_dict['error6'] = "The re-entered password does not match the original password."
  if email.count("@") !=1 or email.count(".") !=1 or len(email) < 3 or len(email) > 20 or " " in email:
    error_dict['error7'] = "Invalid email, please re-enter"
  return error_dict
  
app.run()