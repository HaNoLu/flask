import json,os

from pkg_resources import non_empty_lines

from mysaleapp.saleapp import app


def read_json(path):
    #dong tu dong neu khong, phai f.close
    with open(path, 'r') as f:
        data=json.load(f)
        return data
def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))
def load_products(cate_id=None,kw=None,from_price=None,to_price=None):
    products =read_json(os.path.join(app.root_path, 'data/products.json'))
    if cate_id:
        products = [p for p in products if (p['category_id'])== int(cate_id)]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower())!=-1]
    if from_price:
        products = [p for p in products if p['price']>=float(from_price)]
    if to_price:
        products=[p for p in products if p['price']<=float(to_price)]
    return products
def get_products_by_id(product_id):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))
    for p in products:
        if p['id'] == product_id:
            return p

