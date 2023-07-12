from flask import Blueprint, redirect, render_template, url_for, flash

from forms.user_forms import CreateUserForm

user_views = Blueprint('user', __name__)

@user_views.route('/users/create/')
def create_user():
    form = CreateUserForm()
    return render_template('user/create_user.html',
                           form=form)
                           