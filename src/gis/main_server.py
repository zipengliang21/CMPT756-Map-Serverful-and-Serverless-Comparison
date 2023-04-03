import argparse

from src.gis.service.gis_service import app
from src.gis.service.context import CONTEXT

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Launches a GIS server.")
    parser.add_argument(
        "--gis_db_host", type=str,
        help="The IP address which points to the gis database server.")
    parser.add_argument(
        "--gis_db_user", type=str,
        help="The user of the gis database.")
    parser.add_argument(
        "--gis_db_password",
        type=str,
        help="The password of the gis database user.")

    args = parser.parse_args()

    if args.gis_db_host is None:
        print("gis_db_host is missing.")
        exit(-1)
    if args.gis_db_user is None:
        print("gis_db_user is missing.")
        exit(-1)
    if args.gis_db_password is None:
        print("gis_db_password is missing.")
        exit(-1)

    CONTEXT.Init(gis_db_host=args.gis_db_host,
                 gis_db_user=args.gis_db_user,
                 gis_db_password=args.gis_db_password)
    print(CONTEXT)
    app.run()
