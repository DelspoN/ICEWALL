#!/bin/bash
service php7.0-fpm start
find /var/lib/mysql -type f -exec touch {} \; && service mysql start
mysql -u root < /set.sql
rm /set.sql
mysqladmin -u root password P@ssw0rd123
/usr/sbin/nginx -g "daemon off;"
sleep infinity;
