
from mysaleapp.saleapp.models import Product,Category

def read_json(path):
    pass
def load_categories():
    return Category.query.all()
def load_products(**kwagrs):
    products= Product.query.filter(Product.active.__eq__(True))
    kw=kwagrs.get('kw')
    category_id=kwagrs.get('category_id')
    if category_id:
        products=products.filter(Product.category_id.__eq__(category_id))
    if kw:
        products=products.filter(Product.name.contains(kw))
    from_price=kwagrs.get('from_price')
    if from_price:
        products=products.filter(Product.price.__ge__(from_price))
    to_price=kwagrs.get('to_price')
    if to_price:
        products=products.filter(Product.price.__le__(to_price))
    return products.all()
def get_products_by_id(product_id):
    return Product.query.get(product_id)

