#!/bin/sh

FILE_TO_WATCH="/root/default.conf"
#FILE_DESTINATION_ON_CHANGE="/etc/nginx/http.d/default.conf"
FILE_DESTINATION_ON_CHANGE="/etc/nginx/conf.d/default.conf"

while [[ ! -f '/root/default.conf' ]]; do
  sleep 1
  cp '/var/lib/scratchapp/init-nginx-stateful.conf' "$FILE_TO_WATCH"
done

cp -f $FILE_TO_WATCH $FILE_DESTINATION_ON_CHANGE
lt=`stat -c %Z $FILE_TO_WATCH`;
while true
do 
    at=`stat -c %Z $FILE_TO_WATCH`
    if [[ "$at"  != "$lt" ]]; then 
        cp -f $FILE_TO_WATCH $FILE_DESTINATION_ON_CHANGE
        sleep 1
        nginx -s reload
        lt=$at
        echo `date "+%Y/%m/%d %H:%m:%S"` [reloader] Default config file reloaded
    fi
    sleep 1
done