from db.connections import get_db_connection

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    "SELECT * FROM users WHERE username=%s",
    (username,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    "SELECT * FROM users WHERE id=%s",
    (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    "SELECT id,username,role FROM users",
    )

    user_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return user_list
