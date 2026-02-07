from services.user_services import get_user_by_username
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required
from flask import Blueprint,request
from db.connections import get_db_connection

auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if not username or not password or not confirm_password:
       return {"error":"fields are missing"},400

    if password != confirm_password:
       return {"error":"passwords did not match"},400

    existing_user = get_user_by_username(username)

    if existing_user:
       return {"error": "user already exists"},409

    hashed_password = generate_password_hash(password)

    conn = get_db_connection()
    cursor = conn.cursor()

    if not existing_user:
       cursor.execute(
       "INSERT INTO users(username,password) VALUES (%s,%s)",
       (username,hashed_password)
       )

    conn.commit()
    cursor.close()
    conn.close()
    return{
       "status":"success",
       "username":username
    },201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
       return {"error":"fields are missing"},400

    user = get_user_by_username(username)

    if not user:
       return{"error":"user not found"},404

    if not check_password_hash(user["password"],password):
       return {"error":"Invalid credentials"},401

    access_token = create_access_token(
       identity=str(user["id"]),
       additional_claims={"role":user["role"]}
    )

    refresh_token = create_refresh_token(
       identity=str(user["id"])
     )

    return {
       "access_token":access_token,
       "refresh_token":refresh_token,
       "status":"login successful"
    },200 

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()

    new_access_token = create_access_token(identity=user_id)

    return {
        "access_token": new_access_token
    }, 200
