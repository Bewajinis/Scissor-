from flask import Flask
from flask_restx import Api
from .Auth.views import auth_namespace
from .Shortening.view import short_url
from .Qr.view import Qr_code
from .config.config import config_dict
from .utils import db
from .models.Url import Url
from .models.User import User
from flask_migrate import Migrate
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address




def create_app(config=config_dict['dev']):
    app=Flask(__name__)
    CORS(app)

    app.config.from_object(config)

    migrate = Migrate(app, db)

    api=Api(app)

    limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(short_url, path='/')
    api.add_namespace(Qr_code, path='/')


    db.init_app(app)

  
    @app.route("/")
    @limiter.limit("5/minute") # maximum of 10 requests per minute
    def rateLimiting():
        return "Here is your url"

    
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User': User,
            'Url': Url

        }
        
    
    return app

  