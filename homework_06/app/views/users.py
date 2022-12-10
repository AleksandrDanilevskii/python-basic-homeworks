from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.exceptions import NotFound

from forms.users import CreateUserForm

users_app = Blueprint(
    "users_app",
    __name__,
    # url_prefix="/products",
)


USERS = {
    1: "Bob",
    2: "Sam",
    3: "Nick",
}


@users_app.route("/", endpoint="list")
def users_list():
    return render_template(
        "users/list.html",
        users=USERS,
        # products=PRODUCTS.items(),
    )


@users_app.route("/<int:user_id>/", endpoint="details")
def get_user_by_id(user_id: int):
    user_name = USERS.get(user_id)
    if user_name is None:
        raise NotFound(f"User #{user_id} not found!")
    return render_template(
        "users/details.html",
        user_id=user_id,
        user_name=user_name,
    )


@users_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add_user"
)
def add_user():
    form = CreateUserForm()

    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400

    user_name = form.name.data
    user_id = len(USERS) + 1
    USERS[user_id] = user_name

    # flash(f"Successfully added product {product_name}!")
    url = url_for("users_app.details", user_id=user_id)
    return redirect(url)
