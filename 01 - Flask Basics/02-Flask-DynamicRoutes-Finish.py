from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Tabloids from TCE 19 Berlin!</h1>' #this is actual HTML code!

@app.route('/tableauinfo') #this is the URL path we gonna use to access this page!
def tableauinfo():
    return '<h1>Tableau is the Best!</h1>'

#------- PASTE CODE HERE!! <<< START >>> ------------------
@app.route('/participant/<name>') #this is a dynamic URL that expects a parameter
def participant(name):
    return '<h1>Hello {}, welcome to TCE 19!<h1>'.format(name)
#------- PASTE CODE HERE!! <<< END >>> ------------------

if __name__ == '__main__':
    app.run()
