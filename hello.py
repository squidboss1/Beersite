
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
# db = SQLAlchemy(app)
#
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
#     name = request.form['name']
#     price = request.form['price']
#     quantity = request.form['quantity']
#
#     product = Product(name=name, price=price, quantity=quantity)
#     db.session.add(product)
#     db.session.commit()
#
#     return redirect(url_for('cart'))

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    products = Product.query.all()
    return render_template('cart.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)


