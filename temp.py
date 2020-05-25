from flask import Flask,redirect, url_for, request, render_template,session
import expenditure as db
temp = Flask(__name__)
temp.secret_key="qwefqwefwef"

@temp.route("/")
def index():
	return render_template("index.html")

@temp.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        username = request.form.get('username')
        email=request.form.get('email')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')
        if username == 'admin' and password == "admin" and email=="admin@gmail.com" and confirmpassword=="admin":
            session['admin'] = True
            return redirect(url_for("login"))
        else:
            return redirect(url_for('index',msg="Wrong credentials"))   
	
@temp.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == "admin":
            session['admin'] = True
            return redirect(url_for("add"))
        else:
            return redirect(url_for('signup',msg="Wrong credentials.Password or username doesn't match.You need to create account."))
        
     
        
@temp.route("/add",methods=['GET','POST'])
def add():
    if session.get('admin',0):
        return render_template("add.html")
    else: 
         return redirect(url_for('login',msg="YOU NEED TO LOGIN"))   
     

@temp.route("/add_expenses",methods=['POST'])
def add_expenses():
	amount = request.form['amount']
	category = request.form['category']
	date = request.form['date']
	status = db.add_expenses(amount,category,date)
	return redirect(url_for("ListView",msg=status))

@temp.route("/edit")
def edit():
    if session.get('admin',0):
        return render_template("edit.html")
    else:
         return redirect(url_for('login',msg="YOU NEED TO LOGIN"))
    
@temp.route("/edit_expenses")
def edit_expenses():
    ID=request.form['ID']
    newamount = request.form['newamount']
    newcategory = request.form['newcategory']
    newdate = request.form['newdate']
    status = db.edit_expenses(ID,newamount,newcategory,newdate)
    return redirect(url_for('ListView',msg=status))
	
	
	
@temp.route("/list")
def ListView():
        return render_template("list.html", expenses=db.view_expenses())
        redirect(url_for('InRangeView'))      
        
        
        
@temp.route("/add_range",methods=['POST'])
def add_range():
	startdate = request.form['startdate']
	enddate = request.form['enddate']
	status = db.add_range(startdate,enddate)
	return redirect(url_for('InRangeView',msg=status))
	
	        
@temp.route("/final")
def InRangeView():
        return render_template("final.html", range_amnts=db.amnt_range(),total_amnts=db.total_expenses())  
        #redirect(url_for('TotalView'))      
        
#@app.route("/final")
#def TotalView():
 #      return render_template("final.html", total_amnts=db.total_expenses())
                     
if __name__ == "__main__":
    temp.run(debug=True)      