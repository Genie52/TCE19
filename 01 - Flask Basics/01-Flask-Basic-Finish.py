from flask import Flask

app = Flask(__name__)

#this is our start page!
@app.route('/')

#------- PASTE CODE HERE!! <<< START >>> ------------------
def index():
    return '<h1>Hello Tabloids from TCE 19 Berlin!</h1>' #this is actual HTML code!
#------- PASTE CODE HERE!! <<< END >>> ------------------

#this just means RUN THE APP!! (our web server)
if __name__ == '__main__':
    app.run()
