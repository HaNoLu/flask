from sqlalchemy import  Column,Integer,String,Float,DateTime,ForeignKey,Boolean,Enum
from mysaleapp.saleapp import db
from datetime import datetime
from sqlalchemy.orm import relationship
from enum import Enum as UserEnum
from flask_login import UserMixin
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
class UserRole(UserEnum):
    ADMIN=1
    USER=2

class User(BaseModel,UserMixin):
    __tablename__ = 'user'
    name=Column(String(50),nullable=False)
    username=Column(String(50),nullable=False,unique=True)
    email=Column(String(50),nullable=False)
    password=Column(String(50),nullable=False)
    avatar=Column(String(100),nullable=True)
    active=Column(Boolean,default=True )
    joined_date=Column(DateTime,default=datetime.now)
    user_role=Column(Enum(UserRole),default=UserRole.USER)
    receipts=relationship("Receipt",backref="user",lazy=True)
    def __str__(self):
        return self.name
class Category(BaseModel ):
    __tablename__ = 'category'
    products = relationship("Product",back_populates='category',lazy=True)
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
    category_id=Column(Integer,ForeignKey('category.id'),nullable=False)
    category= relationship("Category", back_populates="products")
    receipt_details=relationship("ReceiptDetails",backref="product",lazy=True)
    def __str__(self):
        return self.name
class Receipt(BaseModel):
    created_date=Column(DateTime,default=datetime.now)
    user_id=Column(Integer,ForeignKey(User.id),nullable=False)
    details=relationship("ReceiptDetails",backref="receipt", lazy=True)
class ReceiptDetails(db.Model):
    receipt_id=Column(Integer,ForeignKey(Receipt.id),nullable=False,primary_key=True)
    product_id=Column(Integer,ForeignKey(Product.id),nullable=False,primary_key=True)
    quantity=Column(Integer,default=0)
    price=Column(Float,default=0)



