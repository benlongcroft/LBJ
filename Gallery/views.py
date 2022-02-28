from flask import Blueprint, render_template
import os
import random
from exif import Image

gallery_blueprint = Blueprint('gallery', __name__, template_folder='templates')


@gallery_blueprint.route('/gallery')
def gallery():
    return render_template("gallery.html", get_image_set=get_image_set)


def get_meta(path):
    with open(path, 'rb') as image_file:
        my_image = Image(image_file)
        if my_image.has_exif:
            return {"make":my_image.make, "model":my_image.model, "datetime": my_image.datetime_original}


def get_image_set():
    image_set = []
    files = os.listdir("./static/assets/gallery")
    assets_path = "assets/gallery"
    random.shuffle(files)
    for x in range(len(files)):
        img_path = files[x]
        if img_path == ".DS_Store":
            continue
        p = os.path.join(assets_path, img_path)
        print(p)
        meta = get_meta("static/"+p)
        image_set.append({'path': p, 'name': get_image_name(p), 'description': None, "meta" : meta})
        # TODO: implement this so that description gets shop metadata
    return image_set


def get_image_name(path):
    return path.split("/")[-1]
