from flask import Flask,render_template,request, redirect, url_for, flash
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

@app.route('/')
def Index():
   all_data = Data.query.all()
   return render_template("index.html", tasks=all_data)

@app.route('/', methods = ['POST'])
def insert():
   if request.method == 'POST':
      task = request.form['task']
      description = request.form['description']
      date = request.form['date']

      my_data = Data(task, description, date)

      db.session.add(my_data)
      db.session.commit()

      flash("Task inserted successfully")

      return redirect(url_for('Index'))

@app.route('/update', methods = ['GET','POST'])
def update():
   if request.method == 'POST':
      my_data = Data.query.get(request.form.get('id'))
      
      my_data.task = request.form['task']
      my_data.description = request.form['description']
      my_data.date = request.form['date']
   
      db.session.commit()
      flash("Task Updated Successfully")

      return redirect(url_for('Index'))

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
   my_data = Data.query.get(id)
   db.session.delete(my_data)
   db.session.commit()
   flash("Employee Deleted Succesfully")

   return redirect(url_for('Index'))

if __name__ == "__main__":
   app.run(debug=True)