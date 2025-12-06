
from mysaleapp.saleapp import app, db,utils
from flask_admin import Admin, BaseView, expose,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from mysaleapp.saleapp.models import Category, Product,UserRole
from flask_login import current_user,logout_user
from flask import redirect,request
class AuthenticationModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)
class ProductView(AuthenticationModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['name']
    column_filters = ('name','price')
    column_list = ('id', 'name', 'price', 'category')
    form_columns = ('name', 'description', 'price', 'active', 'category','image')
    column_labels = {
        'id':'STT',
        'name':'Tên sản phẩm',
        'price':'Giá',
        'category':'Danh mục'
    }
    column_sortable_list = ['id', 'name', 'price', 'category']
class LogOutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self):
        return current_user.is_authenticated
class statsView(BaseView):
    @expose('/')
    def index(self):
        kw=request.args.get('kw')
        from_date=request.args.get('from_date')
        to_date=request.args.get('to_date')
        return self.render('admin/stats.html',stats=utils.product_stats(kw=kw,from_date=from_date,to_date=to_date))
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)
class myAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html',stats=utils.category_stats())
admin = Admin(app=app, name='SaleApp', template_mode='bootstrap4',index_view=myAdminIndexView())
admin.add_view(ProductView(Product, db.session))
admin.add_view(AuthenticationModelView(Category, db.session))
admin.add_view(statsView(name='Thống Kê Doanh Thu'))
admin.add_view(LogOutView(name='logout'))


