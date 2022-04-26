from flask import Blueprint, render_template, flash
from Contact.forms import ContactForm
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Contact.email_secrets import *

contact_blueprint = Blueprint('contact', __name__, template_folder='templates')


def insert_into_template(email, message, rep_name, tel):
    return """<html>
              <body>
                <p>You have a new message from """ + email + """,
                   <br>
                   <div>
                   """ + message + """
                   </div>

                   Telephone: """ + tel + """
                   <br>
                   DO NOT RESPOND TO THIS EMAIL. THIS MAILBOX IS UNMONITORED 
                </p>
              </body>
            </html>"""


def generate_message(email, firstname, lastname, tel, u_message):
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW WEBSITE MAIL: " + firstname + " " + lastname
    message["From"] = email
    message["To"] = recv_email
    html = insert_into_template(email, u_message, tel)
    message.attach(MIMEText(html, "html"))
    return message


def send_mail(form):
    message = generate_message(form.email.data, form.firstname.data,
                               form.lastname.data, form.telephone.data,
                               form.message.data)

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, sender_pswd)
        server.sendmail(sender_email, recv_email, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(e)
        # Print any error messages to stdout
        return False


@contact_blueprint.route('/contact', methods=['POST', 'GET'])
def contact_form():
    form = ContactForm()
    if form.validate_on_submit():
        if send_mail(form):
            return render_template("index.html")
        else:
            flash("Email could not be sent, please try again")
        # then send email
    return render_template("contact.html", form=form)
