from flask import Flask, render_template, request
import dao


app = Flask(__name__)

@app.route('/')
def index():
    q= request.args.get("q")
    cate_id= request.args.get("category_id")
    categories = dao.load_categories()
    products = dao.load_products(q=q, cate_id=cate_id)
    return render_template('index.html', categories=categories, products=products)

@app.route('/products/<id>')
def details(id):
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)