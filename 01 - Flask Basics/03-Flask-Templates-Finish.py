# import Flask library (class) that has needed functionality to build Web Server
# also you need to import render_template - this is library that works with Flask Jinja (HTML) templates
from flask import Flask, render_template

# next we create an instance of this (Flask) class
app = Flask(__name__)

# we then use the route() decorator to tell Flask what URL should trigger our function
# this is out root page!
@app.route('/')
def index():
    return '<h1>Hello Tabloids from TCE 19 Berlin! Welcome to 03 - Templates excercise!</h1>' #this is actual HTML code!

# You can add variable sections to a URL by marking sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument.
# this is a dynamic URL that expects a parameter - eg. http://localhost:5000/participant/Sophie
@app.route('/participant/<name>') #this is a dynamic URL that expects a parameter
def participant(name):
    # we are sending variable 'name' as 'name_html' (you can name it as you like!)
    # to '01-Tableau-NamePass.html' and we can use it to build dynamic HTML content!
    # HTML files are expected to be in 'templates' folder
    return render_template('01-Tableau-NamePass.html',name_html=name)

#------- PASTE CODE HERE!! <<< START >>> ------------------
@app.route('/whereisthefun') #this is a dynamic URL that expects a parameter
def fun():
    where_is_the_fun = "Data Night Out!"
    return render_template('02-Tableau-Fun.html',more_fun_html=where_is_the_fun)
#------- PASTE CODE HERE!! <<< END >>> ------------------

# this just means RUN THE APP!! (our web server)
if __name__ == '__main__':
    app.run()
