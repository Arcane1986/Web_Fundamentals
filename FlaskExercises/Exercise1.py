from flask import Flask

app = Flask(__name__)
app.config["DEBUG"]=True
app.config["ENV"]="development"

@app.route("/")
def index():
  return "Hello World"

app.run(port=8008)