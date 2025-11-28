
from mysaleapp.saleapp.models import Product,Category,User
from mysaleapp.saleapp import app,db
import hashlib
def read_json(path):
    pass
def load_categories():
    return Category.query.all()
def load_products(**kwagrs):
    products= Product.query.filter(Product.active.__eq__(True))
    kw=kwagrs.get('kw')
    from_price = kwagrs.get('from_price')
    to_price = kwagrs.get('to_price')
    category_id=kwagrs.get('category_id')
    page = kwagrs.get('page')

    if category_id:
        products=products.filter(Product.category_id.__eq__(category_id))
    if kw:
        products=products.filter(Product.name.contains(kw))
    if from_price:
        products=products.filter(Product.price.__ge__(from_price))
    if to_price:
        products=products.filter(Product.price.__le__(to_price))

    page_size=app.config['PAGE_SIZE']
    start=(page-1)*page_size
    end=start+page_size
    return products.slice(start,end).all()
def get_products_by_id(product_id):
    return Product.query.get(product_id)
def  count_products():
    return Product.query.filter(Product.active.__eq__(True)).count()
def add_User(username,password,name,**kwagrs):
        password=str(hashlib.md5(password.encode('utf-8')).hexdigest())
        user=User(username=username,
                  password=password,
                  name=name,
                  email=kwagrs.get('email'),
                  avatar=kwagrs.get('avatar'),
                  )
        db.session.add(user)
        db.session.commit()
def check_login(username,password):
    password=str(hashlib.md5(password.encode('utf-8')).hexdigest())
    user=User.query.filter(User.username==username.strip(),
                           User.password==password).first()
    if user:
        return user
def get_user_by_id(user_id):
    return User.query.get(user_id)
