from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_services import get_user_by_id, get_all_users
from utils.rbac import role_required
from services.ai.analyzer import analyze_security

admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/dashboard")
@jwt_required()
@role_required("ADMIN")
def dashboard():
    user_id = int(get_jwt_identity())
    user = get_user_by_id(user_id)
    return{
        "status":"Welcome admin",
        "username":user["username"]
    },200

@admin_bp.route("/get-all-users")
@jwt_required()
@role_required("ADMIN")
def fetch_all_users():
    user_id = int(get_jwt_identity())
    user = get_user_by_id(user_id)

    user_list = get_all_users()

    return {"user list":user_list},200

@admin_bp.route("/security-report", methods=["GET"])
def security_report():
    return analyze_security(), 200
