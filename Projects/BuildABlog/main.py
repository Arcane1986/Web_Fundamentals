from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from config import username,port,password,host,database
from datetime import datetime

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SQLACLHEMY_ECHO']=True

connection_string= f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'


app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
db = SQLAlchemy(app)
db_session = db.session

class Blog(db.Model):
  blog_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  body = db.Column(db.String(1000))
  created_at = db.Column(db.DateTime, default=datetime.now())

@app.route("/")
def index():
  blogs = Blog.query.order_by('blog_id desc').all()
  error = request.args.get('error')
  return render_template('main.html',blogs=blogs,error=error)

@app.route("/newpost", methods=['POST','GET'])
def newpost():
  if request.method == 'GET':
    return render_template('newpost.html')
  if request.method == 'POST':
    new_blog = Blog(**request.form)
    db.session.add(new_blog)
    db.session.commit()
    return redirect("/")

@app.route("/blog")
def individual_post():
  id = request.args.get('id')
  blog = Blog.query.get(id)
  if not blog:
    return redirect("/?error=This Blog does not exist")
  return render_template('blog.html', blog = blog)



if __name__ == "__main__":
    db.create_all()
    app.run()