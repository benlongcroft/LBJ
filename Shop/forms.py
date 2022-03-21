from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, email_validator, ValidationError

def character_check(form, field):
    # checks that first name/last name are valid
    # no special chars
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed!")


class CheckoutForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    address_line1 = StringField(validators=[DataRequired()])
    address_line2 = StringField(validators=[DataRequired()])
    city = StringField(validators=[DataRequired()])
    postcode = StringField(validators=[DataRequired()])
    country = StringField(validators=[DataRequired()])
    submit = SubmitField(validators=[DataRequired()])