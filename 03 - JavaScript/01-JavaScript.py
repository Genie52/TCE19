# import Flask library (class) that has needed functionality to build Web Server
# import render_template - this is library that works with Flask Jinja (HTML) templates
# import request - to access incoming request data, you can use the global request object.
# Flask parses incoming request data for you and gives you access to it through that global object.
# import flask_wtf and wtfforms are libraries that will help us with the form data

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from  wtforms import StringField, SubmitField
import requests

app = Flask(__name__)

# initializin global variables
tableau_ticket_return = ''
username = ''

# this secret key is here a string just so we have forms working - if you want to know more google it ;-)
app.config['SECRET_KEY'] = 'somesecretkey'

# instance the form class - inheritance is from the FlaskForm.
# You can name the calss as you like - we named it "UserForm"
class UserForm(FlaskForm):
    # Below are the form fields we want to be able to capture and send (in our case just the username) to Tableau server.
    # These are used as form attributes in .html file
    # in the quotes is the text user weill see when using the form
    username = StringField("Username:")
    password = StringField("Password:")
    submitForm = SubmitField("Login!")

@app.route('/', methods=['GET','POST']) #make sure you setup GET and POST for our landing page - becaue form will be there ;-)
def index():
    global username
    username = False
    # instance the form! we will send this to our HTML template below in the code
    form = UserForm()

    # check if form is calid on submission (also how to read those form fields)
    if form.validate_on_submit():
        # we are just reading the username! this is because Tableau Server just expects a username as parameter (in this case)
        username = form.username.data
        # in previous line we have already saved the value of username so lets sut reset it to empty string now
        form.username.data = ''
        # now we are referencing the tableau_ticket_return from the top!
        global tableau_ticket_return
        tableau_ticket_return = requests.post("http://localhost/trusted?username=" + username)

    # sending all the variables and form to HTML template
    return render_template('index-tableau.html', form = form, username = username, tableau_ticket_return = tableau_ticket_return)

@app.route('/loginTableauPage')
def loginTableauPage():
    return render_template('loginTableauPage-Finish.html', tableau_ticket = tableau_ticket_return.text, username = username)
    #return render_template('loginTableauPage-Start.html', tableau_ticket = tableau_ticket_return.text, username = username)

if __name__ == '__main__':
    app.run()
