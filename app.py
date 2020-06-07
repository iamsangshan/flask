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
        new_author = request.form['author']

        #model the data
        new_post = BlogPost(title=new_title, content=new_content, author=new_author)
        
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


# Delete functionality
@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

# Edit functionality
@app.route('/posts/edit/<int:id>', methods=["POST", "GET"])
def edit_post(id):
    curr_post = BlogPost.query.get(id)
    # When post is edited and saved
    if request.method == 'POST':
        curr_post.title = request.form['title']
        curr_post.author = request.form['author']
        curr_post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    # When post is being edited, redirect to edit page
    else:
        post=BlogPost.query.get(id)
        return render_template('edit.html', post=curr_post)


# if the app is running in shell command,
# good practise to turn the debug on (dev mode)
if __name__ == "__main__":
    app.run(debug=True)


