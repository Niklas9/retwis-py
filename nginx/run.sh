#!/bin/sh

# NOTE(niklas9):
# * as it's hard to get environments variables directly in nginx configuration,
#   this shellscript is needed -
#   https://gist.github.com/xaviervia/6adea3ddba269cadb794

re="s/<proxy>/$API_PORT_5000_TCP_ADDR:$API_PORT_5000_TCP_PORT/";
cat /nginx_conf/nginx.conf | sed -e $re > /etc/nginx/nginx.conf

nginx -g 'daemon off;'
