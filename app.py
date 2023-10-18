from flask import Flask

app = Flask(__name__) # application instance

@app.route('/') # application route
def index(): # view function
    return 'Weather App!'

if __name__ == '__main__':
    app.run() # programmatitically running Flask