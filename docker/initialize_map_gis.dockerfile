FROM daviesx/756:base

WORKDIR /home/codebase

CMD ["python3",                                                         \
    "-m",                                                               \
    "src.gis.main_initialize_map",                                      \
    "--gis_db_host=gis.cwteclrn492x.ca-central-1.rds.amazonaws.com",    \
    "--gis_db_user=postgres",                                           \
    "--gis_db_password=12345678"]
