from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask_mail import Mail
mail = Mail(app)

from app import views