from db.connections import get_db_connection
from flask import request


def log_login_attempt(username, success):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        ip = request.remote_addr
        user_agent = request.headers.get("User-Agent")

        cursor.execute("""
            INSERT INTO login_logs (username, ip_address, status, user_agent)
            VALUES (%s, %s, %s, %s)
        """, (username, ip, "success" if success else "failed", user_agent))

        conn.commit()

    except Exception as e:
        print("Logging error:", e)

    finally:
        cursor.close()
        conn.close()
