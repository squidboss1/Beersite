from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Product, init_db, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_ECHO'] = True


@app.route('/')
def home():
    s = db.session()
    products = s.query(Product).all()
    return render_template('index.html', products=products)

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


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        print(request.form.to_dict())
        p = Product()
        p.name = request.form['product_name']
        s = db.session()
        s.add(p)
        s.commit()
    return render_template('add_product.jinja2')


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
    # products = Product.query.all()
    return render_template('cart.html', products=products)

@app.route('/initdb')
def initdb():
    db.create_all()

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)


