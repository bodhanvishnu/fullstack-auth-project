from flask_jwt_extended import get_jwt
from functools import wraps

def role_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role")
            if user_role != required_role:
               return {"error":"Access denied"},403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

