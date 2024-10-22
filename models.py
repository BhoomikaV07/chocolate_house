from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    seasonal = db.Column(db.Boolean, default=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(100), nullable=False)
    allergy_concerns = db.Column(db.String(200), nullable=True)
