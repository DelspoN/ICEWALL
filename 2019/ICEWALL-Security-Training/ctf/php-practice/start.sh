#!/bin/bash
service php7.0-fpm start
/usr/sbin/nginx -g "daemon off;"
sleep infinity;
