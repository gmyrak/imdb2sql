FROM mattrayner/lamp

RUN apt-get -y install mc && echo SELECTED_EDITOR="/usr/bin/mcedit" > /root/.selected_editor
RUN mkdir /www && mkdir /www/db.gmda.ru && mkdir /data && mkdir /host && chmod -R 777 /var/lib/mysql-files
COPY files/index.html /www/db.gmda.ru
COPY files/db.gmda.ru.conf /etc/apache2/sites-available
COPY files/dgmyrak-ws.conf /etc/apache2/sites-available
COPY files/sql/* /data/
COPY files/run.sh /run.sh
COPY files/create_database.sh /create_database.sh
RUN chmod +x /create_database.sh
RUN ln -s /etc/apache2/sites-available/db.gmda.ru.conf /etc/apache2/sites-enabled/db.gmda.ru.conf
RUN ln -s /etc/apache2/sites-available/dgmyrak-ws.conf /etc/apache2/sites-enabled/dgmyrak-ws.conf
RUN ln -s /var/www/phpMyAdmin-5.0.2-all-languages /www/db.gmda.ru/phpmyadmin
ENV MYSQL_ADMIN_PASS adminpassw
