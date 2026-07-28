import subprocess
import re


def ping_device(ip):
    """
    Ping a device and return information about its status.
    """

    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    latency = None

    # Search for the latency in the ping output
    match = re.search(
        r"time[=<]?\s*(\d+)\s*ms",
        result.stdout,
        re.IGNORECASE
    )

    if match:
        latency = match.group(1) + " ms"

    return {
        "ip": ip,
        "reachable": result.returncode == 0,
        "latency": latency
    }