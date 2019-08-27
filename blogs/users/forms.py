from flask_wtf  import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed,FileField

from flask_login import current_user
from blogs.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = StringField('Password' , validators=[DataRequired()])
    submit = SubmitField('LogIn')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = StringField('Password' , validators=[DataRequired() , EqualTo('pass_confirm',message="Password must match")])
    pass_confirm = StringField('Confirm Password' , validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if(User.query.filter_by(email = field.data).first()):
            raise ValidationError('Email already registered')

    def check_username(self,field):
        if(User.query.filter_by(username = field.data).first()):
            raise ValidationError('Username already taken')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    # password = StringField('Password' , validators=[DataRequired() , EqualTo('pass_confirm',message="Password must match")])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if(User.query.filter_by(email = field.data).first()):
            raise ValidationError('Email already registered')

    def check_username(self,field):
        if(User.query.filter_by(username = field.data).first()):
            raise ValidationError('Username already taken')


