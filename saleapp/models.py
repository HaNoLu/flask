from sqlalchemy import  Column,Integer,String,Float,DateTime,ForeignKey,Boolean
from mysaleapp.saleapp import db,app
from datetime import datetime
from sqlalchemy.orm import relationship

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel ):
    __tablename__ = 'category'
    product = relationship("Product",backref='category',lazy=True)
    name=Column(String(20),nullable=False)

    def __str__(self):
        return self.name
class Product(BaseModel):
    __tablename__ = 'product'
    name=Column(String(50),nullable=False)
    description=Column(String(255),nullable=True)
    price=Column(Float,default=0)
    image=Column(String(100))
    active=Column(Boolean,default=True )
    created_date=Column(DateTime,default=datetime.now)
    category_id=Column(Integer,ForeignKey(Category.id),nullable=False)
    def __str__(self):
        return self.name
if __name__=='__main__':
    with app.app_context():
        db.create_all()
