from flask import Blueprint, render_template, request, url_for, redirect, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest
from models import User, db

from .forms.users import CreateUserForm

users_app = Blueprint(
    "users_app",
    __name__,
)


USERS = {
    1: "Bob",
    2: "Sam",
    3: "Nick",
}


@users_app.route("/", endpoint="list")
def users_list():
    users = User.query.all()
    return render_template(
        "users/list.html",
        users=users,
    )


@users_app.route("/<int:user_id>/", endpoint="details")
def get_user_by_id(user_id: int):
    user = User.query.get_or_404(
        user_id,
        description=f"User #{user_id} not found!",
    )
    return render_template(
        "users/details.html",
        user=user,
    )


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_user():
    form = CreateUserForm()

    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400

    name = form.name.data
    username = form.username.data
    email = form.email.data
    address = form.address.data
    phone = form.phone.data
    website = form.website.data
    company = form.company.data
    user = User(
        name=name,
        username=username,
        email=email,
        address=address,
        phone=phone,
        website=website,
        company=company,
    )

    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create user {name!r}")

    flash(f"Successfully added user {name}!")
    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
