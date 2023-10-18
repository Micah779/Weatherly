from flask import Flask
from flask import render_template # allows us to render HTML files

app = Flask(__name__) # application instance

@app.route('/') # application route
def index(): # view function
    return render_template('index.html') # renders the index.html file as a view function

if __name__ == '__main__':
    app.run() # programmatitically running Flask