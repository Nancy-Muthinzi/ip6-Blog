from flask import render_template
from .import main

# Views
@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''

    title = 'My Blog'

    return render_template('index.html', title = title)

@main.route('/blog')
def pitch():
    '''
    function that returns the blog details page and its data
    '''
    render_template('blog.html')    

    