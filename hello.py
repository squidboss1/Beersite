from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from models import Product, init_db, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_ECHO'] = True


@app.route('/')
def home():
    s = db.session()
    products = s.query(Product).all()
    return render_template('index.html', products=products)

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


@app.route('/o_nas')
def o_nas():
    return render_template('o_nas.html')


@app.route('/sklep')
def sklep():
    return render_template('sklep.html')


@app.route('/logowanie')
def logowanie():
    return render_template('logowanie.html')

@app.route('/rodzaje_ale')
def rodzaje_ale():
    return render_template('rodzaje_ale.html')
@app.route('/rodzaje_bock')
def rodzaje_bock():
    return render_template('rodzaje_bock.html')
@app.route('/rodzaje_ciemne')
def rodzaje_ciemne():
    return render_template('rodzaje_ciemne.html')
@app.route('/rodzaje_jasne')
def rodzaje_jasne():
    return render_template('rodzaje_jasne.html')
@app.route('/rodzaje_marcowe')
def rodzaje_marcowe():
    return render_template('rodzaje_marcowe.html')
@app.route('/rodzaje_porter')
def rodzaje_porter():
    return render_template('rodzaje_porter.html')
@app.route('/rodzaje_pszeniczne')
def rodzaje_pszeniczne():
    return render_template('rodzaje_pszeniczne.html')
@app.route('/rodzaje_smakowe')
def rodzaje_smakowe():
    return render_template('rodzaje_smakowe.html')
@app.route('/rodzaje_specjalne')
def rodzaje_specjalne():
    return render_template('rodzaje_specjalne.html')
@app.route('/rodzaje_stout')
def rodzaje_stout():
    return render_template('rodzaje_stout.html')
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

@app.route('/rejestracja')
def rejestracja():
    return render_template('rejestracja.html')

@app.route('/koszyk')
def koszyk():
    products = Product.query.all()
    return render_template('koszyk.html', products=products)

@app.route('/karta_zamowienia')
def karta_zamowienia():
    products = Product.query.all()
    return render_template('karta_zamowienia.html', products=products)

@app.route('/initdb')
def initdb():
    db.create_all()

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)


