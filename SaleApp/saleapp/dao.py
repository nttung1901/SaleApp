import json
import hashlib
from model import *



def load_categories():
    # with open('data/categories.json', encoding = 'utf-8') as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, cate_id=None, page =None):
    # with open('data/products.json', encoding = 'utf-8') as f:
    #     products = json.load(f)
    #     if q:
    #         products = [p for p in products if p["name"].find(q)>=0]
    #     if cate_id:
    #         products = [p for p in products if p["category_id"].__eq__(int(cate_id))]
    #     return products
    query = Product.query
    if q:
        query = query.filter(Product.name.contains(q))
    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    if page:
        page_size = app.config["PAGE_SIZE"]
        start = (int(page)-1)*page_size
        query = query.slice(start, start+page_size)
    return query.all()

def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username),
                            User.password.__eq__(password)).first()


def load_product_by_id(id):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)
        for p in products:
            if p["id"].__eq__(int(id)):
                return p


def count_products():
    return Product.query.count()