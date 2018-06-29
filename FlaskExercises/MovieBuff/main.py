from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import username,port,password,host,database

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SQLACLHEMY_ECHO']=True

connection_string= f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'


app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
db = SQLAlchemy(app)
db_session = db.session

class Director(db.Model):
  __tablename__= "directors"

  director_id = db.Column(db.Integer, primary_key=True)
  country = db.Column(db.Text)
  first = db.Column(db.Text)
  last = db.Column(db.Text)

  movies = db.relationship('Movie', backref='directors')

  def __str__(self):
    return f"""Director Table
    Director ID = {self.director_id},
    Country = {self.country},
    First Name = {self.first},
    Last = {self.last}"""

class Viewer(db.Model):
  __tablename__= "viewers"

  viewer_id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text)
  first = db.Column(db.Text)
  last = db.Column(db.Text)

  viewings = db.relationship('Viewing', backref='viewers')

  def __str__(self):
    return f"""Viewer Table
    Viewer ID = {self.viewer_id},
    Email = {self.email},
    First Name = {self.first},
    Last = {self.last}"""

class Viewing(db.Model):
  __tablename__= "viewings"

  viewing_id = db.Column(db.Integer, primary_key=True)
  date_viewed = db.Column(db.Date)
  movie_id = db.Column(db.Integer,db.ForeignKey('movies.movie_id'))
  viewer_id = db.Column(db.Integer, db.ForeignKey('viewers.viewer_id'))

  viewer = db.relationship('Viewer')
  movie = db.relationship('Movie')
  
  def __str__(self):
    return f"""Viewing Table
    Viewing ID = {self.viewing_id},
    Date Viewed = {self.date_viewed},
    Movie ID = {self.movie_id},
    Viewer ID = {self.viewer_id}"""

class Movie(db.Model):
  __tablename__= "movies"

  movie_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text)
  year = db.Column(db.Integer)
  director_id = db.Column(db.Integer, db.ForeignKey('directors.director_id'))

  director = db.relationship('Director')
  
  def __str__(self):
    return f"""Movie Table
    Movie ID = {self.movie_id},
    Title = {self.title},
    Year = {self.year},
    Director ID = {self.director_id}"""

for viewing in Viewing.query.all():
  print(viewing.viewer)
  # print(viewing.movie)

app.run()
  