from flask import render_template
from .import main
from .forms import BlogForm

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

# @app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = ReviewForm()
#     movie = get_movie(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(movie.id,title,movie.poster,review)
#         new_review.save_review()
#         return redirect(url_for('movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)
    