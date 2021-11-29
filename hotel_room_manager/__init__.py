from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bf2bd361-3c2f-4676-97e1-cd85ea71d9de'

    from .views import views

    app.register_blueprint(views, url_prefix = '/')
    return app