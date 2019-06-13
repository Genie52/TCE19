from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from  wtforms import StringField, SubmitField
import requests

app = Flask(__name__)

tableau_ticket_return = ''
username = ''


app.config['SECRET_KEY'] = 'somesecretkey'

# -------------------- 01-PASTE START - FORM variable placeholders -----------------------


# -------------------- 01-PASTE END - FORM variable placeholders -----------------------

@app.route('/', methods=['GET','POST']) #make sure you setup GET and POST for our landing page - becaue form will be there ;-)
def index():
    global username
    username = False
    form = UserForm() #instance the form

# -------------------- 02-PASTE START - FORM data management -----------------------


# -------------------- 02-PASTE END - FORM data management -----------------------

    return render_template('index-tableau.html-Start', form = form, username = username, tableau_ticket_return = tableau_ticket_return)

@app.route('/noLoginTableauPage')
def noLoginTableauPage():
    return render_template('noLoginTableauPage.html')


# -------------------- 03-PASTE START - passing the USERNAME and TICKET to another HTML page -----------------------


# -------------------- 03-PASTE END - passing the USERNAME and TICKET to another HTML page -----------------------

if __name__ == '__main__':
    app.run()
