from flask import Flask
from app.config import Config
from app.routes import skins_bp
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
app.register_blueprint(skins_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
