import math
from flask import render_template,redirect,url_for,request,session,jsonify
from mysaleapp.saleapp import app, utils,login
import cloudinary.uploader
from flask_login import login_user,logout_user


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
@app.context_processor #dùng để toàn bộ hàm khác đề có categories
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
                return redirect(url_for('login'))
            else:
                err_msg="Mật khẩu không trùng khớp"
        except Exception as ex :
            err_msg="Hệ thống đang có lỗi!!!"+str(ex)
    return render_template('register.html',err_msg=err_msg)
@app.route('/login',methods=['GET','POST'])
def login_page():
    err_msg = ""
    if request.method.__eq__('POST'):
        username=request.form.get('username')
        password=request.form.get('password')
        user=utils.check_login(username=username,password=password)
        if user :
            login_user(user=user)
            return redirect(url_for('main'))
        else:
            err_msg="Password of Username is Fasle"
    return render_template('login.html',err_msg=err_msg)

@login.user_loader# tự gọi khi đăng nhập thành công
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)

@app.route('/user-logout')
def logout():
    logout_user()
    return redirect(url_for('login_page'))
@app.route('/api/add_cart',methods=['POST'] )
def add_cart():
    data=request.json
    id=str(data.get('id'))
    name=data.get('name')
    price=float(data.get('price'))

    cart=session.get('cart')
    if not cart:
        cart={}
    if id in cart:
        cart[id]['quantity']=cart[id]['quantity']+1
    else:
        cart[id]={
            'id':id,
            'name':name,
            'price':price,
            'quantity':1
        }
    session['cart']=cart
    return jsonify(utils.get_quantity_cart(cart))