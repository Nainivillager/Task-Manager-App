from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Imp_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/taskmanager'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Data(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   task = db.Column(db.String(50))
   description = db.Column(db.String(100))
   date = db.Column(db.Date)

   def __init__(self, task, description, date):
      self.task = task
      self.description = description
      self.date = date

with app.app_context():
   db.create_all()

@app.route('/')
def Index():
   return render_template("index.html")



if __name__ == "__main__":
   app.run(debug=True)