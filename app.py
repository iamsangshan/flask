from flask import Flask, render_template

#give a name to the app
app = Flask(__name__)

# Our dummy data
stories = [
    {
        'title' : 'Story 1',
        'content' : 'Once upon a time...',
        'author' : 'Sangeetha'
    },
    {
        'title' : 'Story 2',
        'content' : 'And they lived happily everafter...',
        'author' : 'Mvr',
     },

     {
        'title' : 'Story 3',
        'content' : 'That was a bad story...',
     },
]

#add a URL to the app, currently localhost#
#@app.route('/')

#pass an argument to the function and also add additional URL
@app.route('/home/')
def hello() :
    return render_template('index.html')

#pass the stories as a variable to the posts.html
@app.route('/home/posts')
def posts():
    return render_template('posts.html', allstories=stories)

# if the app is running in shell command,
# good practise to turn the debug on (dev mode)
if __name__ == "__main__":
    app.run(debug=True)


