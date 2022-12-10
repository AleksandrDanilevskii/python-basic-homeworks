from flask import Flask, render_template

from views.users import users_app

app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")

app.config.update(
    ENV='development',
    SECRET_KEY='hgjfkdls;a',
)


@app.route('/', endpoint='index_page')
def get_root():
    return render_template("index.html", now='now')


@app.route('/about/', endpoint='about_page')
def get_about():
    return render_template("about.html")
