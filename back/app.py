import connexion
import os
from connexion.resolver import RestyResolver
from flask_cors import CORS
from flask_injector import FlaskInjector

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs
    CORS(app.app, supports_credentials=True)
    app.add_api('api-gateway.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app)
    app.run(port=int(os.environ.get('PORT', 2000)))  # os.environ is handy if you intend to launch on heroku
