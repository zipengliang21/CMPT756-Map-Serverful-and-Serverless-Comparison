import argparse

from src.mutation.init.generate_map import GenerateInitialMap
from src.gis.database.connection import CreateDatabaseConnection
from src.gis.mutation.writer import MutationWriter


def _InitializeMap(gis_db_host: str,
                   gis_db_user: str,
                   gis_db_password: str):
    mutations = GenerateInitialMap()

    db_conn = CreateDatabaseConnection(gis_db_host=gis_db_host,
                                       gis_db_user=gis_db_user,
                                       gis_db_password=gis_db_password)
    writer = MutationWriter(db_conn=db_conn)

    writer.Materialize(requests=mutations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Constructs an initial map definition.")
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

    _InitializeMap(gis_db_host=args.gis_db_host,
                   gis_db_user=args.gis_db_user,
                   gis_db_password=args.gis_db_password)
