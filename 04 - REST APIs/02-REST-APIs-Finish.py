from flask import Flask, render_template, request
from flask_wtf import FlaskForm #import flask from
from  wtforms import StringField, SubmitField #use string and submit for the form
import requests

import tableauserverclient as TSC



app = Flask(__name__)

#global variables
tableau_ticket_return = ''
username_global = ''
matching_user = ''
workbook_list = list()



#tableau REST API login
tableau_auth = TSC.TableauAuth('admin', 'admin')
server = TSC.Server('http://localhost', use_server_version = True) #use_server_version = True gives us the latest REST API version to work with

server.auth.sign_in(tableau_auth)  #sign in to Tableau Server and do the things below

#lets get the tableau version!
tableau_server_version =  server.version
print('Tableau Server Version:', server.version,'\n') #3.2 is 2018.3

#get all the workbooks!
all_workbooks, all_workbooks_pagination_item = server.workbooks.get()
print([workbook.name for workbook in all_workbooks]) #get it nice in the list
#print it one below another
for workbook in all_workbooks:
    print(workbook.name)

#this secret key is here a string just so we have forms working - if you want to know more google it
app.config['SECRET_KEY'] = 'somesecretkey'

#instance the form class - inheritance is from the FlaskForm. You can name the calss as you like - we named it "UserForm"
class UserForm(FlaskForm):
    #below are the form fields we want to be able to capture and send (in our case just the username) to Tableau server. These are used as form attributes in .html file
    #in the quotes is the text user weill see when using the form
    username = StringField("Username:")
    password = StringField("Password:")
    submitForm = SubmitField("Login!")


@app.route('/', methods=['GET','POST']) #make sure you setup GET and POST for our landing page - becaue form will be there ;-)
def index():
    username = False
    form = UserForm() #instance the form

    #check if form is calid on submission (also how to read those form fields)
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = '' #in previous line we have already saved the value of username so lets sut reset it to empty string now
        form.password.data = ''
        global tableau_ticket_return #now we are referencing the tableau_ticket_return from the top!
        tableau_ticket_return = requests.post("http://localhost/trusted?username=" + username)

        global username_global
        username_global = username

        #get user by name - this is how we gonna filter user by Username
        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                     TSC.RequestOptions.Operator.Equals,
                                     username))
        global matching_user
        global workbook_list
        workbook_list.clear() #make sure list is clean before we add() elements

        #get the user we want with the req_option prepared filter from above
        matching_user, pagination_item = server.users.get(req_option)
        server.users.populate_workbooks(matching_user[0]) #u need to populate workbooks to be ablet to browse them

        #show logged in user and its LUID
        print('Active username: ',matching_user[0].name, ' and its LUID: ', matching_user[0].id)

        #now lets go thru available workbooks for above user
        for workbook in matching_user[0].workbooks :
            #print(workbook.name, workbook.content_url)
            server.workbooks.populate_views(workbook)
            workbook_list.append(workbook)
            print('\nViews of the Workbook uder ID: ',workbook.id, ' (name : ',workbook.name,')' ,' are: ',[view.name for view in workbook.views])

    #just a test to see in console workbooks and views
    for item in workbook_list:
        print("\nWorkbook: ", item.name)
        for view in item.views:
            print("View:", view.name)


    return render_template('index-tableau.html', form = form, username = username, tableau_ticket_return = tableau_ticket_return)
    #return render_template('index-tableau.html', username = username)

@app.route('/listOfWorkbooks')
def loginTableauPage():
    return render_template('listOfWorkbooks-Finish.html', tableau_ticket = tableau_ticket_return, username = username_global, tableau_server_version = tableau_server_version, all_workbooks = all_workbooks, matching_user = matching_user, workbook_list = workbook_list)

if __name__ == '__main__':
    app.run()
