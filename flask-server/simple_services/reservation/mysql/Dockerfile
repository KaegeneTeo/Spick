FROM mysql:latest

ENV MYSQL_DATABASE=${MYSQL_DATABASE} \
    MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}

ADD reservation.sql /docker-entrypoint-initdb.d

EXPOSE 9999