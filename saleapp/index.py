import math
from flask import render_template, Flask,redirect,url_for,request
from mysaleapp.saleapp import app, utils
import cloudinary.uploader

@app.route('/')
def main():
    categories=utils.load_categories()
    category_id=request.args.get('category_id')
    kw=request.args.get('keyword')
    counter=utils.count_products()
    page = request.args.get('page', 1, int)
    products=utils.load_products(category_id=category_id,kw=kw,page=page)
    return render_template('index.html',
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
@app.context_processor
def common_response():
    return {
        'categories':utils.load_categories(),
    }
@app.route('/products/<int:product_id>')
def product_profile(product_id):
    product = utils.get_products_by_id(product_id=product_id)
    return  render_template('product_detail.html',product=product)
@app.route('/register',methods=['GET','POST'])
def register():
    err_msg=""
    categories = utils.load_categories()
    if request.method.__eq__('POST'):
        name=request.form.get('name')
        username=request.form.get('username')
        password=request.form.get('password')
        email=request.form.get('email')
        comfirm=request.form.get('comfirm')
        avatar=request.files.get('avatar')
        avatar_path=None
        try:

            if(password.strip().__eq__(comfirm.strip())):
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path=res['secure_url']
                utils.add_User(name=name.strip(),
                               username=username.strip(),
                               password=str(password.strip()),
                               email=email,
                               avatar=avatar_path,)
                return redirect(url_for('main'))
            else:
                err_msg="Mật khẩu không trùng khớp"
        except Exception as ex :
            err_msg="Hệ thống đang có lỗi!!!"+str(ex)
    return render_template('register.html',err_msg=err_msg)

