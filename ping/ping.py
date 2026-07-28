import subprocess


def ping_device(ip):
    """
    Ping a device and return information about its status.
    """

    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    return {
        "ip": ip,
        "reachable": result.returncode == 0
    }