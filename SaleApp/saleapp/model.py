from itertools import product

from sqlalchemy import Column,Integer,String,Boolean,Float,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import user
from unicodedata import category

from saleapp import app, db


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique= True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50),nullable=False)
    avatar = Column(String(200),default="https://res.cloudinary.com/dqe19i7og/image/upload/v1731659931/pngtree-account-avatar-user-abstract-circle-background-flat-color-icon-png-image_1650938_xqovwm.jpg")
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.name

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique= True)
    products = relationship('Product', backref='Category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique= True)
    price = Column(Float,default=0)
    image = Column(String(200), default="https://res.cloudinary.com/dqe19i7og/image/upload/v1730955526/apple-iphone-16-ultramarine_jj1lxj.webp")
    category_id= Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        c1 = Category(name = "Mobile")
        c2 = Category(name = "Tablet")
        c3 = Category(name = "Laptop")
        db.session.add_all([c1,c2,c3])
        db.session.commit()
        import json
        with open('data/products.json', encoding='utf-8') as f:
            products = json.load(f)
            for p in products:
                prod = Product(**p)
                db.session.add(prod)
            db.session.commit()
        import hashlib
        u = User(name="tungnguyen", username = "admin",
                 password=str(hashlib.md5("123".encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
