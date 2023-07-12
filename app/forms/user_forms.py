from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired
class CreateUserForm(FlaskForm):
    username = StringField('username' ,
                           validators=[DataRequired()])
    email = EmailField('Email',
                   validators=[DataRequired()])   
    password = PasswordField('password',
                   validators=[DataRequired()])   
    
