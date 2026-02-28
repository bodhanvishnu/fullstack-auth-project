def calculate_risk(signals):
    score = 0

    if signals["failed_attempts"] >= 5:
        score += 50

    if signals["unique_ips"] > 3:
        score += 25

    if signals["rapid_failures"]:
        score += 25

    if score >= 75:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level
