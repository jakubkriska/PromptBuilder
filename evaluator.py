def log_evaluation(variant, filepath="outputs/evaluation_log.json"):
    import json, os
    from datetime import datetime

    log = {"variant": variant, "timestamp": datetime.utcnow().isoformat()}

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)