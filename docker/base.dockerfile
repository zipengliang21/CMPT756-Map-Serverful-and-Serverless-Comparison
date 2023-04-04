FROM ubuntu:23.04

RUN apt update && apt upgrade -y

RUN apt install -y      \
    protobuf-compiler   \
    python3             \
    python3-boto3       \
    python3-flask       \
    python3-protobuf    \
    python3-psycopg2    \
    python3-pip         \
    wget                \
    zip

WORKDIR /home

# Downloads the codebase.
ADD https://api.github.com/repos/zipengliang21/CMPT756-Map-Serverful-and-Serverless-Comparison/commits?per_page=1 latest_commit
RUN wget https://codeload.github.com/zipengliang21/CMPT756-Map-Serverful-and-Serverless-Comparison/zip/refs/heads/main
RUN unzip main && rm main
RUN mv CMPT756-Map-Serverful-and-Serverless-Comparison-main codebase
