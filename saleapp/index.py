from flask import render_template, Flask
from mysaleapp.saleapp import app
from mysaleapp.saleapp import utils
@app.route('/')
def main():
    cates=utils.load_categories()
    return render_template('index.html',cat=cates)
@app.route('/products')
def products_list():
    products=utils.load_products()
    return render_template('products.html',products=products)
if __name__=='__main__':
    app.run(debug=True)