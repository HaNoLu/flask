
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.secret_key='hsakjfhhafkahfhkdkjfahkehkfhk3hk3hkh3k13198yrhif'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Admin%40123@localhost:3306/saleappdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 8

db=SQLAlchemy(app=app)
from mysaleapp.saleapp import models
from mysaleapp.saleapp import  index
