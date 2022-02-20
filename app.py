from flask import Flask, render_template
from Gallery.views import get_image_set
from Shop.views import get_shop_image

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5jE6y9MTmkCGqWRaBF7fz4'
app.config['RECAPTCHA_PUBLIC_KEY'] = "6LekrNocAAAAAJmeku5jE6y9MTmkCGqWRaBF7fz4"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6LekrNocAAAAAPGHhArtwxjfv1p-TC1C1VNGmQCO"


# HOME PAGE VIEW
@app.route('/')
def start():
    return render_template('splash.html')


@app.route('/index')
def index():
    return render_template('index.html', get_image_set=get_image_set)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/shop')
def shop():
    return render_template("shop.html", get_shop_images=get_shop_image)


@app.errorhandler(400)
def bad_request(error):
    return render_template('error/400.html'), 400


@app.errorhandler(403)
def page_forbidden(error):
    return render_template('error/403.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error/500.html'), 500


if __name__ == '__main__':
    app.run()
