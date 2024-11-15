from sqlalchemy import Column,Integer,String,Boolean,Float,ForeignKey
from saleapp import app, db


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50),nullable=False)
    avatar = Column(String(200),default="https://res.cloudinary.com/dqe19i7og/image/upload/v1731659931/pngtree-account-avatar-user-abstract-circle-background-flat-color-icon-png-image_1650938_xqovwm.jpg")
    active = Column(Boolean = True, nullable=False)

    def __str__(self):
        return self.name

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(Float,default=0)
    image = Column(String(200), default="https://res.cloudinary.com/dqe19i7og/image/upload/v1730955526/apple-iphone-16-ultramarine_jj1lxj.webp")
    category_id= Column()

    def __str__(self):
        return self.name

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # c1 = Category(name = "Mobile")
        # c2 = Category(name = "Laptop")
        # c3 = Category(name = "Tablet")
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()