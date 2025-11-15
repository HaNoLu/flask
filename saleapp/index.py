
from flask import render_template, Flask,redirect,url_for,request
from mysaleapp.saleapp import app, utils

@app.route('/')
def main():
    categories=utils.load_categories()
    category_id=request.args.get('category_id')
    kw=request.args.get('keyword')
    products=utils.load_products(category_id=category_id,kw=kw)
    return render_template('index.html',categories=categories,products=products)
@app.route('/products')
def products_list():
    category_id=request.args.get('category_id')
    kw=request.args.get('keyword')
    from_price=request.args.get('from_price')
    to_price=request.args.get('to_price')
    products = utils.load_products(category_id=category_id,kw=kw,from_price=from_price ,to_price=to_price)
    return render_template('products.html',products=products)
@app.route('/products/<int:product_id>')
def product_profile(product_id):
    product = utils.get_products_by_id(product_id=product_id)
    return  render_template('product_detail.html',product=product)

