def generate_explanation(signals, level):
    if level == "HIGH":
        return "Multiple failed login attempts from several IP addresses indicate possible brute-force attack."

    if level == "MEDIUM":
        return "Suspicious login activity detected. Monitor closely."

    return "No suspicious behavior detected."
