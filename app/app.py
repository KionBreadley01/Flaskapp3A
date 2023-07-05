from flask import (Flask, render_template, request,
                   redirect, url_for, flash)
from db.categories import Category
app = Flask(__name__)

@app.route('/')
@app.route('/homme/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/categories/')
def categories():
    categories = Category.get_all()
    return render_template('categories.html', 
                           categories=categories)

@app.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        if not category:
            flash('Debes ingresar la categoria')
        elif not description:
            flash('Debes ingresar la description')
        else:
            cat = Category(category, description)
            cat.save()
            return redirect(url_for('categories'))

    return render_template('create_cat.html')

    

if __name__ == '__main__':
    app.run(debug=True)