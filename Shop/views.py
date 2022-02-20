from flask import Blueprint
import os

shop_blueprint = Blueprint('shop', __name__, template_folder='templates')


def get_shop_image():
    imgs = []
    path = "./static/assets/shop"
    items = os.listdir(path)
    assets_path = "assets/shop"
    used = []
    for item in items:
        if item == ".DS_Store":
            continue
        f_path = os.path.join(path, item)
        a_path = os.path.join(assets_path, item)
        img_paths = os.listdir(f_path)
        for x in img_paths:
            imgs.append({'path': os.path.join(a_path, x), 'name': get_image_name(x), 'description': None})
    return imgs


def get_image_name(path):
    return path.split("/")[-1]
