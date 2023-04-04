import argparse
from flask_cors import CORS

from src.navigation.service.navigation_service import app
from src.navigation.service.context import CONTEXT

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Launches a Navigation server.")
    parser.add_argument(
        "--navigation_db_host", type=str,
        help="The IP address which points to the navigation database server.")
    parser.add_argument(
        "--navigation_db_user", type=str,
        help="The user of the navigation database.")
    parser.add_argument(
        "--navigation_db_password",
        type=str,
        help="The password of the navigation database user.")

    args = parser.parse_args()

    if args.navigation_db_host is None:
        print("navigation_db_host is missing.")
        exit(-1)
    if args.navigation_db_user is None:
        print("navigation_db_user is missing.")
        exit(-1)
    if args.navigation_db_password is None:
        print("navigation_db_password is missing.")
        exit(-1)

    CONTEXT.Init(navigation_db_host=args.navigation_db_host,
                 navigation_db_user=args.navigation_db_user,
                 navigation_db_password=args.navigation_db_password)
    CORS(app)
    app.run(host="0.0.0.0")
