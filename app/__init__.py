from flask import Flask
from flask_uploads import IMAGES, UploadSet, configure_uploads
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos', IMAGES)

# App Initialization
def create_app(config_name):
    app = Flask(__name__)
    
    # Create app config
    app.config.from_object(config_options[config_name])
    
    # configure uploads
    configure_uploads(app, photos)
    
    # Flask extensions Initialization
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # Blueprint registering
    from .main import main as main_blueprint
    from .auth import auth as authentication_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(authentication_blueprint, url_prefix='/authenticate')
    
    return app