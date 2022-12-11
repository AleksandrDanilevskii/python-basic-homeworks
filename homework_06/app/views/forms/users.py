from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateUserForm(FlaskForm):
    name = StringField(
        label="Name",
        name="name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    username = StringField(
            label="Username",
            name="username",
            validators=[
                DataRequired(),
                Length(min=3),
            ],
        # render_kw={'class': 'form-control'}
    )
    email = StringField(
        label="Email",
        name="email",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    address = TextAreaField(
        label="Address",
        name="address",
        default='',
    )
    phone = StringField(
        label="Phone",
        name="phone",
        default='',
    )
    website = StringField(
        label="Website",
        name="website",
        default='',
    )
    company = StringField(
        label="Company",
        name="company",
        default='',
    )
