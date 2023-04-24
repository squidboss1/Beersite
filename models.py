from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    current_stock = db.Column(db.Integer)
    image_path = db.Column(db.Text)


def init_db(app):
    db.init_app(app)
