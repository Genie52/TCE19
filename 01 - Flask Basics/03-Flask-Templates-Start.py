from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Tabloids from TCE 19 Berlin! Welcome to 03 - Templates excercise!</h1>' #this is actual HTML code!


@app.route('/participant/<name>')
def participant(name):
    return render_template('01-Tableau-NamePass.html',name_html=name)

#------- PASTE CODE HERE!! <<< START >>> ------------------

#------- PASTE CODE HERE!! <<< END >>> ------------------

if __name__ == '__main__':
    app.run()
