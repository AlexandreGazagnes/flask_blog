from flask import Blueprint, render_template, request
from flasblog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """home/main page """

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    """about page, general info regarding the project """

    return render_template('about.html', title='About')
