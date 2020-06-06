from flask import Flask

#give a name to the app
app = Flask(__name__)

#add a URL to the app, currently localhost#
#@app.route('/')

#pass an argument to the function and also add additional URL
@app.route('/home/<string:person>')
def hello(person) :
    return "Hello, Welcome " + person + " !"
# if the app is running in shell command,
# good practise to turn the debug on (dev mode)
if __name__ == "__main__":
    app.run(debug=True)


