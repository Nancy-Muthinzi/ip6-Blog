from flask import render_template,request,redirect,url_for,abort
from .import main
from .forms import CommentForm,UpdateProfile
from ..models import Comment, User
from flask_login import login_required
from .. import db,photos

# Views
@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''

    title = 'My Blog'

    return render_template('index.html', title = title)

@main.route('/blog/<int:id>')
def blog():
    '''
    function that returns the blog details page and its data
    '''
    render_template('blog.html')    

@main.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):

    form = CommentForm()

    # blog = get_blog(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = comment(blog.id,comment)
        new_comment.save_comment()
        return redirect(url_for('blog',id = blog.id ))

    title = f'{blog.title} comment'
    return render_template('new_comment.html',title = title, comment_form=form, blog=blog)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    
