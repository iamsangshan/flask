from flask import Flask

#give a name to the app
app = Flask(__name__)

#add a URL to the app, currently localhost
@app.route('/')
def hello() :
    return "Hello World. This is a FLask App!"
# if the app is running in shell command,
# good practise to turn the debug on (dev mode)
if __name__ == "__main__":
    app.run(debug=True)

