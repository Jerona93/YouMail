import os #para las variables de entorno y apis

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        FROM_EMAIL=os.environ.get('FROM_EMAIL'),
        MAILJET_API_KEY=os.environ.get('MAILJET_API_KEY'),
        MAILJET_API_SECRET=os.environ.get('MAILJET_API_SECRET'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    from . import db

    db.init_app(app)
    
    from . import mail

    app.register_blueprint(mail.bp)

    return app