from flask import Flask, render_template,request,session
import random
from datetime import date
app=Flask(__name__)
app.config["SECRET_KEY"]="235#2009"


   


@app.route('/unitconverter')
def unitconverter():
    return render_template('unitconverter.html')

@app.route('/validateconverter')
def validateconverter():
    unitconverter = request.args.get("unitconverter",type=int)
    unit=unitconverter*10000000
    return render_template('unitconverter.html',result=unit)

@app.route('/vowelchecker')
def vowelchecker():
    return render_template('vowelchecker.html')

@app.route('/validatevowelchecker')
def validatevowelchecker():
    vowel = request.args.get("vowelchecker")
    if vowel.lower() in ['a','e','i','o','u']:        
        return ('the letter you have entered is a vowel.')
    else:
        return ('the letter you have entered is not a vowel.')

@app.route('/marksavrage')
def marksavrage():
    return render_template('marksaverage.html')

@app.route('/validatemarks')
def validatemarks():
    maths=request.args.get('maths',type=int)
    science=request.args.get('science',type=int)
    english=request.args.get('english',type=int)
    hindi=request.args.get('hindi',type=int)
    socialscience=request.args.get('socialscience',type=int)
    avrage=(maths+science+english+hindi+socialscience)/5
    return render_template('marksaverage.html',result=avrage)
@app.route('/courior_programe', methods=['GET', 'POST'])
def courior_programe():
    if request.method=='GET':
        return render_template("courior_programe.html")
    if request.method=='POST':
        weight=request.form.get("weight",type=float)
    if weight<=20:
        if weight==20:
            price=weight*10
        elif weight>=10:
            price=weight*12
        elif weight>=1:
            price=weight*14
        elif weight<1:
            price="free of cost!"
    else:
        price="we cannot deliver your package, it is too heavy"
    return render_template("courior_programe.html",result=price) 

quotes=['A reader lives a thousand lives before he dies.',
'A person who never reads lives only once.',
'never trust a person who has\'nt read a book',
'You Can find Magic wherever you LOOK. Sit back and Relax, all you Need is a BOOK',
'The more that you READ, the more things you will KNOW. The more that you LEARN, the more places you\'ll GO.']

quote=random.choice(quotes)    
             
@app.route('/', methods=['GET', 'POST'])
def password():
    if request.method=="GET":
        return render_template("password.html")
    password=request.form.get("password")
    username=request.form.get("username")
    session["username"]=username
    message="Hello to access the website please enter the password!"
    print(password)
    if password=="Jr7+2m21":
        return render_template("index.html",quote=quote)
    else:
        return render_template('password.html',error="incorrect password")
    

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("readersclubhomepage.html")

@app.route('/library', methods=['GET', 'POST'])
def library():
    return render_template("access_library.html")

@app.route('/about_school', methods=['GET', 'POST'])
def about_school():
    return render_template("about_school.html")

@app.route('/form_cert', methods=['GET', 'POST'])
def form_cert():
    if request.method=="GET":
        return render_template("formto_cert.html")
    firstname=request.form.get("fname")
    lastname=request.form.get("lname")
    coursename=request.form.get("cname")
    today = date.today()
    print (coursename)
    print (firstname)
    return render_template("certificate.html",name=firstname+lastname,coursename=coursename,date=today)


    
    return render_template("password.html",message=message)



if __name__ == "__main__":
    app.run(debug=True)

