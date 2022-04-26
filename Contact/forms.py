from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, Email
import re


def character_check(form, field):
    # checks that first name/last name are valid
    # no special chars
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed!")


def phone_check(form, field):
    # checks phone number is valid format
    p = re.compile(r'\+?\d{10}')
    if not p.match(field.data):
        raise ValidationError(f'Phone number must be in format +XXXXXXXXXX!')


class ContactForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    telephone = StringField(validators=[DataRequired(), phone_check])
    message = TextAreaField(validators=[DataRequired(), Length(max=500)])
    submit = SubmitField(validators=[DataRequired()])