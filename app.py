from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///student.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class student(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    desc=db.Column(db.String,nullable=False)
    date_date=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
@app.route("/",methods=['GET','POST'])
def html():
    if request.method=='POST':
       title=request.form['titles']
       desc=request.form['descs']
       Student=student(title=title,desc=desc)
       db.session.add(Student)
       db.session.commit()
    allstudent=student.query.all()
    return render_template("index.html",allstudent=allstudent)


@app.route('/delete/<int:sno>')
def delete(sno):
    students=student.query.filter_by(sno=sno).first()
    db.session.delete(students)
    db.session.commit()
    return redirect('/') 

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        titl = request.form['title']
        desc = request.form['desc']
        Student = student.query.filter_by(sno=sno).first()
        Student.title = titl
        Student.desc = desc
        db.session.add(Student)
        db.session.commit()
        return redirect("/")
    Studen=student.query.filter_by(sno=sno).first()
  
    return render_template('update.html',Student=Studen)


    
    



if __name__ == "__main__":
    app.run(debug=True,port=5002)



   