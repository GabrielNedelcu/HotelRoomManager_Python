from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bf2bd361-3c2f-4676-97e1-cd85ea71d9de'

    from .routes import routes

    app.register_blueprint(routes, url_prefix='/')

    # db.init_connection()

    return app
