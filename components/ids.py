def detect_intrusion(logs):
    alerts = []
    for log in logs:
        if "FAILED LOGIN" in log:
            alerts.append("Brute force detected")
    return alerts
