FROM ubuntu:latest
LABEL authors="pavlo"

ENTRYPOINT ["top", "-b"]