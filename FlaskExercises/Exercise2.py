class Rxcase:
  def __init__(self,request_type,drug_name,request_date):
    self.case_number=Rxcase.increment_counter()
    self.request_type=request_type
    self.drug_name=drug_name
    self.request_date=request_date

  def __repr__(self):
    return f"Rxcase({self.case_number},{self.request_type},{self.drug_name},{self.request_date})"

  def __str__(self):
    return f"Case Number: {self.case_number}, Request Type: {self.request_type}, Drug Name: {self.drug_name}, Request Date: {self.request_date}"

  counter = 0

  @classmethod
  def increment_counter(cls):
    cls.counter += 1
    return cls.counter

from flask import Flask,request

app = Flask(__name__)
app.config["DEBUG"]=True
app.config["ENV"]="development"

storage=[]

@app.route("/")
def index():
  return f"""
  <form action="/submit" method="POST">
    <p>Case Number: {Rxcase.counter+1}</p>
    <p><select name="request_type">
      <option value="Coverage Determination">Coverage Determination</option>
      <option value="Redetermination">Redetermination</option>
      <option value="CD DMR">CD DMR</option>
      <option value="RD DMR">RD DMR</option>
    </select></p>
    <p>Drug Name
    <input type="text" name="drug_name"></p>
    <p>Request Date
    <input type="datetime-local" name="request_date">
    <input type="submit" value="Create"></p>
  </form>
  """

@app.route("/submit",methods=["POST"])
def store_data():
  form_data = request.form
  req_type = form_data["request_type"]
  drug_nam = form_data["drug_name"]
  req_date = form_data["request_date"]

  rx_case_instance = Rxcase(req_type,drug_nam,req_date)
  storage.append(rx_case_instance)
  print(storage)
  return """Neato!!!
  <br><br><br>
  <a href="http://127.0.0.1:8008/">Home</a><br>
  <a href="http://127.0.0.1:8008/display">Data</a><br>"""

@app.route("/display")
def display():
  final_str=""
  for item in storage:
    final_str=final_str+str(item)+"<br>"
  return final_str

app.run(port=8008)

