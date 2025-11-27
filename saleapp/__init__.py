
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cloudinary
app=Flask(__name__)
app.secret_key='hsakjfhhafkahfhkdkjfahkehkfhk3hk3hkh3k13198yrhif'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Admin%40123@localhost:3306/saleappdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 8

db=SQLAlchemy(app=app)
from mysaleapp.saleapp import models
from mysaleapp.saleapp import  index
cloudinary.config(
            cloud_name= "diwuthkyv",
            api_key= "563232354487514",
            api_secret= "aZ3jvQ6oQxg_uUM0bNlTb9liy_8",
)