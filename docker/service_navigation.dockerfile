FROM daviesx/756:base

WORKDIR /home/codebase

CMD ["python3",                                                                     \
    "-m",                                                                           \
    "src.gis.main_server",                                                          \
    "--navigation_db_host=navigation.cwteclrn492x.ca-central-1.rds.amazonaws.com",  \
    "--navigation_db_user=postgres",                                                \
    "--navigation_db_password=12345678"]
