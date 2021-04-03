from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    user = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate=db.Column(db.String(250), nullable=False)
    population=db.Column(db.Integer, nullable=False)
    orbital_period=db.Column(db.Integer, nullable=False)
    rotation_period=db.Column(db.Integer, nullable=False)
    diameter=db.Column(db.Integer, nullable=False)
    planet= db.Column(db.Boolean, db.ForeignKey('favorite.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "name": self.name,
            "population": self.population,
            "orbital_period": self.orbital_period
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth=db.Column(db.String(250), nullable=False)
    gender=db.Column(db.String(250))
    height=db.Column(db.Integer, nullable=False)
    skin=db.Column(db.String(250), nullable=False)
    eye=db.Column(db.String(250), nullable=False)
    character= db.Column(db.Boolean, db.ForeignKey('favorite.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "name": self.name,
            "birth": self.birth,
            "height": self.height
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    planets = db.relationship('Planet', backref='favorite', lazy=True)
    characters = db.relationship('Character', backref='favorite', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "name": self.name,
            "birth": self.birth,
            "height": self.height
            # do not serialize the password, its a security breach
        }