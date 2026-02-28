def extract_signals(logs):
    failed = [l for l in logs if l["status"] == "failed"]
    success = [l for l in logs if l["status"] == "success"]

    ips = set(l["ip_address"] for l in logs)

    return {
        "failed_attempts": len(failed),
        "success_attempts": len(success),
        "unique_ips": len(ips),
        "rapid_failures": len(failed) >= 5
    }
