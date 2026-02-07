from flask import Blueprint,request
from services.user_services import get_user_by_id
from flask_jwt_extended import get_jwt_identity,jwt_required

user_bp = Blueprint("user",__name__)

@user_bp.route("/dashboard")
@jwt_required()
def dashboard():
    user_id = int(get_jwt_identity())
    username = get_user_by_id(user_id)
    return {
       "status":"successfully accessed dashboard",
       "username":username["username"]
    }

@user_bp.route("/profile")
@jwt_required()
def profile():
    user_id = int(get_jwt_identity())
    user = get_user_by_id(user_id)
    return {
       "status":"profile found",
       "username":user["username"],
       "user id":user["id"],
       "user role":user["role"]
    }
