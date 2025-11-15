import math

from flask import render_template, Flask,redirect,url_for,request
from mysaleapp.saleapp import app, utils

@app.route('/')
def main():
    categories=utils.load_categories()
    category_id=request.args.get('category_id')
    kw=request.args.get('keyword')
    counter=utils.count_products()
    page = request.args.get('page', 1, int)
    products=utils.load_products(category_id=category_id,kw=kw,page=page)
    return render_template('index.html',
                           categories=categories,
                           products=products,
                           pages=math.ceil(counter/app.config['PAGE_SIZE']))
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

