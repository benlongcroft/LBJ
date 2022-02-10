from flask import Flask, render_template
from datetime import timedelta
from flask_talisman import Talisman

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=45)
app.config['SECRET_KEY'] = '5jE6y9MTmkCGqWRaBF7fz4'
app.config['RECAPTCHA_PUBLIC_KEY'] = "6LekrNocAAAAAJmeku5jE6y9MTmkCGqWRaBF7fz4"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6LekrNocAAAAAPGHhArtwxjfv1p-TC1C1VNGmQCO"

csp = {
    'default-src': [
        '\'self\'',
        'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css'
    ],
    'script-src': [
        '\'self\'',
        '\'unsafe-inline\''
        'https://www.google.com/recaptcha/',
        'https://www.gstatic.com/recaptcha/'
    ],
    'frame-src': [
        'https://www.google.com/recaptcha/',
        'https://recaptcha.google.com/recaptcha/'
    ]
}

talisman = Talisman(app, content_security_policy=csp)


# HOME PAGE VIEW
@app.route('/')
def index():
    return render_template('index.html')


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
