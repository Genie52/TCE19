# import Flask library (class) that has needed functionality to build Web Server
from flask import Flask

# next we create an instance of this (Flask) class
app = Flask(__name__)

# we then use the route() decorator to tell Flask what URL should trigger our function
# this is out root page!
@app.route('/')
def index():
    return '<h1>Hello Tabloids from TCE 19 Berlin!</h1>' #this is actual HTML code!

# this is the URL path we gonna use to access this page! eg. http://localhost:5000/tableauinfo
@app.route('/tableauinfo')
def tableauinfo():
    return '<h1>Tableau is the Best!</h1>'

# You can add variable sections to a URL by marking sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument.
#------- PASTE CODE HERE!! <<< START >>> ------------------
# this is a dynamic URL that expects a parameter - eg. http://localhost:5000/participant/Sophie
@app.route('/participant/<name>')
def participant(name):
    return '<h1>Hello {}, welcome to TCE 19!<h1>'.format(name)
#------- PASTE CODE HERE!! <<< END >>> ------------------

# this just means RUN THE APP!! (our web server)
if __name__ == '__main__':
    app.run()
