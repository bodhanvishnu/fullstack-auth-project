from db.connections import get_db_connection
from services.ai.signals import extract_signals
from services.ai.risk_engine import calculate_risk
from services.ai.explanation import generate_explanation


def fetch_recent_logs(limit=50):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT username, ip_address, status, created_at
        FROM login_logs
        ORDER BY created_at DESC
        LIMIT %s
    """, (limit,))

    logs = cursor.fetchall()
    cursor.close()
    conn.close()

    return logs


def analyze_security():
    logs = fetch_recent_logs()
    signals = extract_signals(logs)
    score, level = calculate_risk(signals)
    message = generate_explanation(signals, level)

    return {
        "risk_score": score,
        "risk_level": level,
        "signals": signals,
        "message": message
    }
