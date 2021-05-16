#!/bin/bash


/usr/bin/mysqld_safe > /dev/null 2>&1 &

RET=1
while [[ RET -ne 0 ]]; do
    echo "=> Waiting for confirmation of MySQL service startup (create DB)"
    sleep 5
    mysql -uroot -e "status" > /dev/null 2>&1
    RET=$?
done

mysql  -uadmin -p${MYSQL_ADMIN_PASS}  < /data/world.sql
mysql  -uadmin -p${MYSQL_ADMIN_PASS}  < /data/sakila-schema.sql
mysql  -uadmin -p${MYSQL_ADMIN_PASS}  < /data/sakila-data.sql
mysql  -uadmin -p${MYSQL_ADMIN_PASS}  < /data/imdb.sql
