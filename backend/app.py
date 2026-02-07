from admin.admin import admin_bp
from routes.auth import auth_bp
from routes.user import user_bp
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from datetime import timedelta
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 900
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

jwt = JWTManager(app)

app.register_blueprint(auth_bp,url_prefix="/auth")
app.register_blueprint(user_bp,url_prefix="/user")
app.register_blueprint(admin_bp,url_prefix="/admin")

@app.route("/")
def home():
    return {"status":"project is working"},200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5006)
