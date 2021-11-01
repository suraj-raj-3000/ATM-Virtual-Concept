from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///atm_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class user_registration(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    pwd_again = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.name} - {self.email}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        f_name = request.form['name']
        e_mail = request.form['email_address']
        pwd = request.form['pwd']
        re_pwd = request.form['re_pwd']
        atm_data = user_registration(name=f_name, email=e_mail, pwd=pwd, pwd_again=re_pwd)
        db.session.add(atm_data)
        db.session.commit()
    all_data = user_registration.query.all()
    return render_template('index.html', var_data=all_data)


# @app.route("/product", methods=['GET', 'POST'])
# def product():
#     all_data = user_registration.query.all()
#     print(all_data)
#     return "<p>Hello, this is product page !</p>"

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        f_name = request.form['name']
        e_mail = request.form['email_address']
        pwd = request.form['pwd']
        re_pwd = request.form['re_pwd']
        update_data = user_registration.query.filter_by(sno=sno).first()
        update_data.name = f_name
        update_data.email = e_mail
        update_data.pwd = pwd
        update_data.pwd_again = re_pwd
        db.session.add(update_data)
        db.session.commit()
        return redirect("/")

    update_data = user_registration.query.filter_by(sno=sno).first()
    return render_template('update.html', var_data=update_data)
    
@app.route("/delete/<int:sno>")
def delete(sno):
    del_data = user_registration.query.filter_by(sno=sno).first()
    db.session.delete(del_data)
    db.session.commit()
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug='true', port=8000)
