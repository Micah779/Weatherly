from flask import Flask

app = Flask(__name__) # application instance

@app.route('/') # application route
def index(): # view function
    return 'Weather App!'

@app.route('/<name>')
def print_name(name):
    return 'Hi, {}'.format(name)

if __name__ == '__main__':
    app.run() # programmatitically running Flask