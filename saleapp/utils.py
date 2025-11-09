import json,os
from mysaleapp.saleapp import app


def read_json(path):
    #dong tu dong neu khong phai f.close
    with open(path, 'r') as f:
        data=json.load(f)
        return data
def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))
def load_products():
    return read_json(os.path.join(app.root_path, 'data/products.json'))