import flask
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from werkzeug.utils import secure_filename
import random
import smtplib as s
import json
import os

with open('config.json', 'r') as c:
    params = json.load(c) ["params"]
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_PHOTO'] = params['photo_location']
app.config['UPLOAD_DOC'] = params['doc_location']
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///atm_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

# ------------random pin generate--------
r_pin = random.randint(1000, 9999)

class tranjection(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    atm_number = db.Column(db.String(17))
    account_number = db.Column(db.String(20))
    tranjection_no = db.Column(db.Integer, unique=True)
    Status = db.Column(db.String(20))
    debit_ammount = db.Column(db.Integer)
    credit_ammount = db.Column(db.Integer)
    tranjection_date = db.Column(db.DateTime)
    

    def __repr__(self) -> str:
        return f"{self.tranjection_no} - {self.Status} - {self.debit_ammount} - {self.credit_ammount} - {self.tranjection_date}"

class user_account(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(50), nullable=False)
    branch_name = db.Column(db.String(100), nullable=False)
    ifsc_code = db.Column(db.String(20), nullable=False)
    account_number = db.Column(db.String(20), unique=True)
    account_balance = db.Column(db.Integer, nullable=False)
    atm_number = db.Column(db.String(17), unique=True)
    cvv = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    marital_status = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.Integer, nullable=False)
    pan_number = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    id_proof_type = db.Column(db.String(100), nullable=False)
    id_proof_number = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    pin_code = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(500), nullable=False)
    nominee_req = db.Column(db.String(50), nullable=False)
    n_full_name = db.Column(db.String(100))
    n_relation = db.Column(db.String(100))
    n_date_of_birth = db.Column(db.String(50), nullable=False)
    n_address = db.Column(db.String(200))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    pin = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.account_type} - {self.branch_name} - {self.ifsc_code} - {self.account_number} - {self.account_balance} - {self.atm_number} - {self.cvv} - {self.expiry_date} - {self.title} - {self.full_name} - {self.father_name} - {self.mother_name} - {self.gender} - {self.marital_status} - {self.mobile_number} - {self.pan_number} - {self.date_of_birth} - {self.email} - {self.id_proof_type} - {self.id_proof_number} - {self.address} - {self.state} - {self.district} - {self.pin_code} - {self.photo} - {self.nominee_req} - {self.n_full_name} - {self.n_relation} - {self.n_date_of_birth} - {self.n_address} - {self.create_date} - {self.pin} "

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    
    return render_template('index.html')

def uploader():
    u = request.files['user_photo']
    # id_proof = request.files['id_proof_file_type']
    u.save(os.path.join(app.config['UPLOAD_PHOTO'], secure_filename(u.filename)))
    # id_proof.save(os.path.join(app.config['UPLOAD_DOC'], secure_filename(id_proof.filename)))
    return "done"

#  ----------------Create User Route And function ----------------------#

@app.route("/create_account", methods=['GET', 'POST'])

def create_account():
    if request.method == 'POST':
        account_type = request.form['account_radio_btn']
        branch_name = request.form['select_branch']
        ifsc_code = request.form['ifsc_code_box']
        account_number = request.form['account_no']
        account_balance = 20000
        atm_number = request.form['atm_no']
        cvv = request.form['cvv']
        expiry_date = request.form['showDate']
        title = request.form['title']
        full_name = request.form['fname']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        gender = request.form['gender_radio_btn']
        marital_status = request.form['married_radio_btn']
        mobile_number = request.form['phone_number']
        pan_number = request.form['pan_number']
        date_of_birth = request.form['date_of_birth']
        email = request.form['email']
        id_proof_type = request.form['id_proof']
        id_proof_number = request.form['id_proof_number']
        address = request.form['address']
        state = request.form['inputState']
        district = request.form['dist']
        pin_code = request.form['pin_code']

        photo = request.files['user_photo']
        ph_name = ("user/pic/" + photo.filename)

        nominee_req = request.form['Nominee_radio_btn']
        n_full_name = request.form['nomi_name']
        n_relation = request.form['select_relation']
        n_date_of_birth = request.form['nimi_dob']
        n_address = request.form['nomi_address']
        create_date = datetime.now()
        pin = random.randint(1000, 9999)

        d_o_b = request.form['date_of_birth']
        print(d_o_b)
        account_data = user_account(account_type = account_type, branch_name = branch_name, ifsc_code = ifsc_code, account_number = account_number, account_balance = account_balance, atm_number = atm_number, cvv = cvv, expiry_date = expiry_date, title = title, full_name = full_name, father_name = father_name, mother_name = mother_name, gender = gender, marital_status = marital_status, mobile_number = mobile_number, pan_number = pan_number, date_of_birth = date_of_birth, email = email, id_proof_type = id_proof_type, id_proof_number = id_proof_number, address = address, state = state, district = district, pin_code = pin_code, photo = ph_name, nominee_req = nominee_req, n_full_name = n_full_name, n_relation = n_relation, n_date_of_birth = n_date_of_birth, n_address = n_address, create_date=create_date, pin=pin)
        db.session.add(account_data)
        db.session.commit()
    #-----------saving photo and document -------------
        uploader()
    # ----------------send pin using email ---------------
        ob=s.SMTP("smtp.gmail.com",587)
        ob.starttls()
        ob.login("masterwork.suraj@gmail.com", "Suraj@150399")

        subject="Citi Bank Account open succefully"
        body=("Hello "+ str(full_name) + "\n Your Account Bank Account open succefully \n\n Your Account number is:" + str(account_number) + "\n Your Atm number is:" + str(atm_number) + "\n Your Pin is:" + str(pin) + "\n\n Thank you for choseing citi bank !")
        massage="Subject:{}\n\n{}".format(subject,body)
        ob.sendmail("masterwork.suraj@gmail.com",email,massage)
        flash("Atm number and pin send to your mail","success")
        ob.quit()

        return render_template('index.html')
   
    return render_template('create_account.html')
    
    # --------------------- tranjection ---------------

def withdraw_tranjection(atm_number):
  
    tranjection_no = random.randint(1000000000, 9999999999)
    atm_num = atm_number
    q1 = user_account.query.filter_by(atm_number=atm_number).first()
    print(q1)
    account_number = q1.account_number
    status = "debited"
    debit_ammount = request.form.get('withdrawable_ammount')
    tranjection_date = datetime.now()

    query = tranjection(tranjection_no = tranjection_no, atm_number=atm_num, Status=status, debit_ammount=debit_ammount, tranjection_date=tranjection_date)

    db.session.add(query)
    db.session.commit()
    return "done"

def deposit_tranjection(acc_num):
  
    tranjection_no = random.randint(1000000000, 9999999999)
    ac_num = acc_num
    status = "credit"
    credit_ammount = request.form.get('deposit_ammount')
    tranjection_date = datetime.now()

    query = tranjection(tranjection_no = tranjection_no, account_number=ac_num, Status=status, credit_ammount=credit_ammount, tranjection_date=tranjection_date)

    db.session.add(query)
    db.session.commit()
    return "done"
# -------------------admin login route ---------------

@app.route('/admin', methods=['GET', 'POST'])
def do_admin_login():
    if ('user' in session and session['user'] =="admin"):
        all_user = user_account.query.all()[-5:]
        tot_ammount = db.session.query(db.func.sum(user_account.account_balance)).first()
        t_ammount = remove_extra_char(str(tot_ammount))
        tot_account = db.session.query(db.func.count(user_account.sno)).first()
        t_account = remove_extra_char(str(tot_account))
        return render_template('dashboard.html', all_user=all_user, varriable1=t_ammount, varriable2=t_account)
         
    username = request.form['admin_username']
    password = request.form['admin_password']
    if username == 'admin' and password == 'password':
        #set session variable
        session['user'] = username 
        all_user = user_account.query.all()[-5:]
        tot_ammount = db.session.query(db.func.sum(user_account.account_balance)).first()
        tot_account = db.session.query(db.func.count(user_account.sno)).first()
        t_ammount = remove_extra_char(str(tot_ammount))
        t_account = remove_extra_char(str(tot_account))
        flash("Welcome back admin!", "success")
        return render_template('dashboard.html',all_user=all_user, varriable1=t_ammount, varriable2=t_account)
        
    return render_template('index.html')
# -------------------admin logout route ---------------

@app.route('/logout', methods=['GET','POST'])
def admin_logout():
    session.pop('user')
    return redirect('/')
# -------------------user login route ---------------


@app.route('/home', methods=['GET', 'POST'])
def do_user_login():
    
    atm_num = request.form.get('card_no')
    atm_pin = str(request.form.get('atm_pin'))
    query = user_account.query.filter_by(atm_number=request.form.get('card_no')).first()

    if query:
        print(query)
        if str(query.pin) == str(request.form.get('atm_pin')):
            query = user_account.query.filter_by(atm_number=atm_num).first()
            mini = tranjection.query.all()
            all_data = user_account.query.all()
            return render_template('home.html', query=query, mini=mini, all_data=all_data)

        return render_template('index.html') 
    flash("Login Failed please check your input","danger")
    return render_template('index.html')

    #  ----------------Create home And its function ----------------------#

# --------------------- Fund Transfer ---------------- #
@app.route("/fund_transfer", methods=['GET', 'POST'])
def fund_transfer():
    if request.method == "POST":
        ac_num = request.form.get('acc_number_fund')
        atm_pin = str(request.form['atm_pin_fund'])

        from_query = user_account.query.filter_by(account_number=ac_num).first()

        to_ac_num = request.form.get('acc_number_to')
        to_query = user_account.query.filter_by(account_number=to_ac_num).first()
        
        if from_query:
            if str(from_query.pin) == str(request.form.get('atm_pin_fund')):

                transfer_ammount = request.form.get('transfer_ammount')
                # f_ammount = 
                # to_ammount = 
                f_ammount = from_query.account_balance - int(transfer_ammount)
                to_ammount = to_query.account_balance + int(transfer_ammount)

                from_query.account_balance = f_ammount
                to_query.account_balance = to_ammount
                db.session.add(from_query,to_query)
                db.session.commit()

                flash("Fund  Successfully Transfered", "success")
                return redirect('/')
        flash("fund transfer failed", "success")
        return render_template('index.html') 
    return render_template('update.html')
# ----------------Pin change -------------------
@app.route("/update_pin", methods=['GET', 'POST'])
def pin_change():
    if request.method == "POST":
        atm_num = request.form.get('card_num')
        atm_pin = str(request.form.get('atm_pin'))
        query = user_account.query.filter_by(atm_number=atm_num).first()
        if query:
            if str(query.pin) == str(request.form.get('atm_pin')):
                withdrawable_ammount = request.form.get('deposit_ammount')
                query = user_account.query.filter_by(atm_number=atm_num).first()
                query.pin = int(request.form.get('new_pin'))
                db.session.add(query)
                db.session.commit()
                flash("Pin Changed Successfully", "success")
                return redirect('/')
        
        return render_template('index.html') 
    return render_template('update.html')
# ----------------withdraw -------------------
@app.route("/withdraw", methods=['GET', 'POST'])
def withdraw_ammount():
    if request.method == "POST":
        atm_num = request.form.get('card_no')
        atm_pin = str(request.form['atm_pin'])
        query = user_account.query.filter_by(atm_number=atm_num).first()
        if query:
            if str(query.pin) == str(request.form['atm_pin']):
                withdrawable_ammount = request.form['withdrawable_ammount']
                query = user_account.query.filter_by(atm_number=atm_num).first()
                query.account_balance = query.account_balance - int(withdrawable_ammount)
                db.session.add(query)
                db.session.commit()

                withdraw_tranjection(atm_num)

                flash("Withdraw Success", "success")
                return redirect('/')

        return render_template('index.html') 
    return render_template('update.html')

# ----------------Deposit -------------------
@app.route("/deposit", methods=['GET', 'POST'])
def Deposit_ammount():
    if request.method == "POST":
        acc_num = request.form.get('account_number')
        atm_pin = str(request.form.get('atm_pin'))
        query = user_account.query.filter_by(account_number=acc_num).first()
        if query:
            if str(query.pin) == str(request.form.get('atm_pin')):
                withdrawable_ammount = request.form.get('deposit_ammount')
                query = user_account.query.filter_by(account_number=acc_num).first()
                query.account_balance = query.account_balance + int(withdrawable_ammount)
                db.session.add(query)
                db.session.commit()
                deposit_tranjection(acc_num)
                flash("Deposit Success", "success")
                return redirect('/')

        return render_template('index.html') 
    return render_template('update.html')

    #  ----------------Create Admin Route And function ----------------------#

@app.route("/viewaccount", methods=['GET', 'POST'])
def viewaccount():
    all_user = user_account.query.all()
    return render_template('table.html', all_user=all_user)

@app.route("/user", methods=['GET', 'POST'])
def user():
    return render_template('user.html')

def remove_extra_char(test_string):
    bad_chars = ['(', ')', ',', "*"]
    for i in bad_chars :
        test_string = test_string.replace(i, '')
    return test_string    
if __name__ == "__main__":
    app.run(debug='true', port=8080)
