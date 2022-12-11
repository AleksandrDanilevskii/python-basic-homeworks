from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from request_test_users import get_users_from_api
from views.users import users_app
from models import db, User


app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")

app.config.update(
    ENV="development",
    SECRET_KEY="hgjfkdls;a",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:password@localhost:5432/postgres",
)

csft = CSRFProtect(app)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.cli.command("db-create-test-users")
def db_create_test_users():
    """
    Создание тестовых пользователей из метода https://jsonplaceholder.typicode.com/users
    """
    users_json = get_users_from_api()
    users = [
        User(
            name=user_json["name"],
            username=user_json["username"],
            email=user_json["email"],
            address=user_json["address"],
            phone=user_json["phone"],
            website=user_json["website"],
            company=user_json["company"],
        )
        for user_json in users_json
    ]
    db.session.add_all(users)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest("Could not create test users")


@app.route("/", endpoint="index_page")
def get_root():
    return render_template("index.html", now="now")
