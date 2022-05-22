FROM openresty/openresty:alpine-fat

RUN mkdir /var/log/nginx
RUN touch /var/log/nginx/error.log

RUN apk add --no-cache openssl-dev
RUN apk add --no-cache git
RUN apk add --no-cache gcc
RUN luarocks install lua-resty-openidc

COPY './config' '/var/lib/scratchapp'
ENTRYPOINT ["/bin/sh", "/var/lib/scratchapp/starter.sh"]
#ENTRYPOINT ["/usr/local/openresty/nginx/sbin/nginx", "-g", "daemon off;"]
EXPOSE 80