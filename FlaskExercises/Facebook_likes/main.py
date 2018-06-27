from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

names = []

@app.route('/', methods=["POST","GET"])
def index():
  if len(names) == 0:
    statement = "No ones likes this."
  else: 
    statement = likes(names)
  return render_template('like_form.html', statement = statement)

@app.route('/add', methods=["POST"])
def like():
  names.append(request.form['first-name'])
  return redirect('/')

def likes(list):
  if len(list)==0:
    statement = "No ones likes this."
  elif len(list)==1:
    statement = f"{list[0]} likes this."
  elif len(list)==2:
    statement = f"{list[0]} and {list[1]} like this."
  elif len(list)==3:
    statement = f"{list[0]}, {list[1]} and {list[2]} like this."
  else:
    list_length = len(list)-2
    statement = f"{list[0]}, {list[1]} and {list_length} like this."
  return statement
  
app.run()