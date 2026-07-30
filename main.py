from cli.arguments import parse_arguments
from services.network_service import (
    run_all,
    run_ping,
    run_ssh,
    run_report,
)


def main():

    args = parse_arguments()

    if args.ping:

        run_ping()

    elif args.backup:

        run_ssh()

    elif args.report:

        report_data = run_ping()
        run_report(report_data)

    elif args.all:

        run_all()

    else:

        # Default behavior
        run_all()


if __name__ == "__main__":
    main()