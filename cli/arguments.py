import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Network Automation Toolkit"
    )

    parser.add_argument("--ping", action="store_true", help="Ping all devices")
    parser.add_argument("--backup", action="store_true", help="Create configuration backups")
    parser.add_argument("--report", action="store_true", help="Generate the CSV report")
    parser.add_argument("--all", action="store_true", help="Run all operations")

    return parser.parse_args()