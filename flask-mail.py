from flask import Flask, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "",  #Mail address,
    "MAIL_PASSWORD": "",  #Mail password
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route("/mail", methods=["GET"])
def get_qrcode():
    subject = request.args.get('subject')  #title
    body = request.args.get('body')  #body
    recipients = request.args.get('recipients')  #to

    msg = Message(subject=subject,
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients=[recipients],
                  body=body)
    mail.send(msg)
    return "200"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)