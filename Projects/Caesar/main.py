import Caesar
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
  return render_template('form.html', secret_text="")

@app.route("/encrypt", methods = ["POST"])
def rotate_string():
  rot = int(request.form['rot'])
  text = request.form['text']
  secret_text = Caesar.encrypt(text,rot)
  return render_template("form.html", secret_text=secret_text)

app.run()