import argparse

from src.mutation.init.generate_map import GenerateInitialMap
from src.navigation.database.connection import CreateDatabaseConnection
from src.navigation.mutation.writer import MutationWriter


def _InitializeMap(
        navigation_db_host: str, navigation_db_user: str,
        navigation_db_password: str):
    mutations = GenerateInitialMap()

    db_conn = CreateDatabaseConnection(
        navigation_db_host=navigation_db_host,
        navigation_db_user=navigation_db_user,
        navigation_db_password=navigation_db_password)

    writer = MutationWriter(db_conn=db_conn)

    writer.Materialize(requests=mutations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Constructs an initial map definition.")
    parser.add_argument(
        "--navigation_db_host", type=str,
        help="The IP address which points to the navigation database server.")
    parser.add_argument(
        "--navigation_db_user", type=str,
        help="The username of the navigation postgres database.")
    parser.add_argument(
        "--navigation_db_password",
        type=str,
        help="The password of the navigation postgres database user.")

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

    _InitializeMap(navigation_db_host=args.navigation_db_host,
                   navigation_db_user=args.navigation_db_user,
                   navigation_db_password=args.navigation_db_password)
