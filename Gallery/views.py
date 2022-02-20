from flask import Blueprint
import os
import random

gallery_blueprint = Blueprint('gallery', __name__, template_folder='templates')


def get_image_set():
    image_set = []
    files = os.listdir("./static/assets/gallery")
    assets_path = "assets/gallery"
    used = []
    for x in range(10):
        num = random.randint(0, len(files) - 1)
        if num in used:
            continue
        used.append(num)
        img_path = files[num]
        print(img_path.split(".")[-1])
        if img_path == ".DS_Store":
            continue
        p = os.path.join(assets_path, img_path)
        print(p)
        image_set.append({'path': p, 'name': get_image_name(p)})
    return image_set


def get_image_name(path):
    return path.split("/")[-1]
