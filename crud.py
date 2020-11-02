"""CRUD operations."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """gets all users"""

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)
    #get function only takes in primary key

def get_user_by_email(user_email):

    return User.query.filter(User.email == user_email).first()
    #email is not a primary key, need to specify first request

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """gets all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):

    return Movie.query.get(movie_id)

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user_rel=user, movie_rel=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)