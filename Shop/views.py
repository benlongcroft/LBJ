from flask import Blueprint, render_template, request, flash
from app import db
from models import Products
from Shop.forms import CheckoutForm

shop_blueprint = Blueprint('shop', __name__, template_folder='templates')


# def get_item_info():
#     imgs = []
#     path = "./static/assets/shop"
#     items = os.listdir(path)
#     assets_path = "assets/shop"
#     for item in items:
#         if item == ".DS_Store":
#             continue
#         f_path = os.path.join(path, item)
#         a_path = os.path.join(assets_path, item)
#         img_paths = os.listdir(f_path)
#         for x in img_paths:
#             imgs.append({'path': os.path.join(a_path, x), 'name': get_image_name(x), 'description': None, 'cost': None})
#     return imgs

@shop_blueprint.route('/shop')
def shop():
    return render_template("shop.html", get_shop_images=get_all_items)


@shop_blueprint.route('/product', methods=['GET'])
def product_page():
    pid = request.args.get('prod', type=int)
    return render_template("product_page.html", product=get_product(pid))


@shop_blueprint.route('/checkout', methods=['POST'])
def checkout():
    form = CheckoutForm()
    size = [item for key, item in request.form.items()]
    pid = request.args.get("pid", type=int)
    product = get_product(pid)
    if not size:
        flash("You must choose a size!")
        return render_template("product_page.html", product=product)
    else:
        return render_template("checkout.html", item={'size': size[0], 'product':product}, form=form)

# @shop_blueprint.route("/success", methods=['POST'])
# def submit_checkout():
#     if form.validate_on_submit():
#         flash("Form Submitted!")
#         return render_template("checkout.html", item={'size': size[0], 'product':product}, form=form)

def get_product(pid):
    return Products.query.filter_by(product_id=pid).first()


def get_all_items():
    d = []
    results = db.session.query(Products.product_id, Products.image_path, Products.name,
                               Products.colour, Products.cost,
                               Products.description).all()

    for row in results:
        if row.image_path == None:
            continue
        print(row.image_path)
        d.append(
            {'product_id': row.product_id, 'path': row.image_path, 'name': row.name,
             'colour': row.colour,
             'description': row.description, 'cost': str(row.cost) + "0"})
    return d


def get_image_name(path):
    return path.split("/")[-1].split(".")[0]
