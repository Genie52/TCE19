# import Flask library (class) that has needed functionality to build Web Server
from flask import Flask

# next we create an instance of this (Flask) class
app = Flask(__name__)

# we then use the route() decorator to tell Flask what URL should trigger our function
# this is out root page!
@app.route('/')

# The function is given a name (it can be any function name! - in this case we named it 'index')
# which is also used to generate URLs for that particular function,
# and returns the message we want to display in the user’s browser.
#------- PASTE CODE HERE!! <<< START >>> ------------------
def index():
    return '<h1>Hello Tabloids from TCE 19 Berlin!</h1>' #this is actual HTML code!
#------- PASTE CODE HERE!! <<< END >>> ------------------

#this just means RUN THE APP!! (our web server)
if __name__ == '__main__':
    app.run()
