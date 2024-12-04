FROM apache/superset:latest

USER root

# Install system dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev pkg-config build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install mysqlclient

ENV ADMIN_USERNAME $ADMIN_USERNAME
ENV ADMIN_EMAIL $ADMIN_EMAIL
ENV ADMIN_PASSWORD $ADMIN_PASSWORD

COPY /config/superset_init.sh ./superset_init.sh
RUN chmod +x ./superset_init.sh

COPY /config/superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py
ENV SECRET_KEY $SECRET_KEY

USER superset

ENTRYPOINT [ "./superset_init.sh" ]