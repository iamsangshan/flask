from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#give a name to the app
app = Flask(__name__)


#Create an SQLite DB

# 1. Set DB type to SQLite or anything
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# 2. create our DB
db = SQLAlchemy(app)

# 3. Database Modeling
class BlogPost(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable= False, default='Unknown')
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    # Method to print
    def __repr__(self):
        return "Blog post " + str(self.id)

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
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    # if user is posting something
    if request.method == 'POST':

        #get the data
        new_title = request.form['title']
        new_content = request.form['content']

        #model the data
        new_post = BlogPost(title=new_title, content=new_content)
        
        #add to DB
        db.session.add(new_post)

        #make it persistent
        db.session.commit()

        #come back to the page
        return redirect('/posts')
    
    #if user is not posting anything, just display the current blog posts
    else:
        stories = BlogPost.query.all()
        return render_template('posts.html', allstories=stories)

# if the app is running in shell command,
# good practise to turn the debug on (dev mode)
if __name__ == "__main__":
    app.run(debug=True)


