import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["fav_car"]=request.form['fav_car']
    session["fav_food"]=request.form['fav_food']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["fav_movie"]=request.form['fav_movie']
    #and session["fav_movie"] not in session
    return render_template('page3.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    session["fav_state"]=request.form['fav_state']

    count = 0

    if ( session['fav_car'] == "The Prius"):
      AC1=": True"
      count+=1
    else:
      AC1=": False"

    if ( session['fav_food'].lower() == "pizza"):
      AC2=": True"
      count+=1
    else:
      AC2=": False"

    if ( session['fav_movie'].lower() == "the lion king"):
      AC3=": True"
      count+=1
    else:
      AC3=": False"

    if ( session['fav_state'].lower() == "solid"):
      AC4=": True"
      count+=1
    else:
      AC4=": False"

    return render_template('page4.html', AC1 = AC1, AC2 = AC2, AC3 = AC3, AC4 = AC4, count = count)


#String myStr1 = "Hello";
#String myStr2 = "HELLO";
#String myStr3 = "Another String";
#System.out.println(myStr1.equalsIgnoreCase(myStr2)); // true
#System.out.println(myStr1.equalsIgnoreCase(myStr3)); // false




if __name__=="__main__":
    app.run(debug=True)
