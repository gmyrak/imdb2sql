FROM mattrayner/lamp

RUN mkdir /www && mkdir /www/db.gmda.ru && mkdir /data && mkdir /host && chmod -R 777 /var/lib/mysql-files
COPY files/index.html /www/db.gmda.ru
COPY files/db.gmda.ru.conf /etc/apache2/sites-available
RUN ln -s /etc/apache2/sites-available/db.gmda.ru.conf /etc/apache2/sites-enabled/db.gmda.ru.conf

RUN ln -s /var/www/phpMyAdmin-5.0.2-all-languages /www/db.gmda.ru/phpmyadmin
ENV MYSQL_ADMIN_PASS adminpassw
ENV MYSQL_USER_NAME user
ENV MYSQL_USER_PASS upass