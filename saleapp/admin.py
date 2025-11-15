from mysaleapp.saleapp import app, db
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView
from mysaleapp.saleapp.models import Category, Product


admin = Admin(app=app, name='SaleApp', template_mode='bootstrap4')
class ProductView(ModelView):
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


# ... sau đó thêm view này


class CategoryView(ModelView):
    column_list = ('id', 'name')
    form_columns = ('name',)
admin.add_view(ProductView(Product, db.session))
admin.add_view(CategoryView(Category, db.session))

