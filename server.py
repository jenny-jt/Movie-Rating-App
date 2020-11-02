"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """View homepage."""

    if 'current_user' in session:
        current_user = session['current_user']
    else:
        current_user = session['current_user'] = '' 
    
    if session['current_user'] != '':
        flash(f'User {current_user} logged in!')

    return render_template('homepage.html')

#session = {
#    'cur-user': user_id
#}
@app.route('/login', methods=['POST'])
def login():
    """Log user into app."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        if user.password == password:
            session['current_user'] = user.user_id
            return redirect('/')
        else:
            flash('Wrong password!')
            session['current_user'] = ''
            return redirect('/')

    else:
        flash('Email not in system. Would you like to create a new user?')
        return redirect('/')

@app.route('/movies')
def all_movies():
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_users():
    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""

    email =request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route('/users/<user_id>')
def show_user(user_id):
    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
