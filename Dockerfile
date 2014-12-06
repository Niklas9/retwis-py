FROM debian:wheezy
MAINTAINER Niklas Andersson <nandersson900@gmail.com>

RUN apt-get -y update && apt-get -y upgrade
# installing apt-get packages for flask and redis here instead of using
# requirements.txt, due to its smaller filesize footprint
RUN apt-get install -y python-flask python-redis

EXPOSE 5000

ADD . /code
WORKDIR /code

CMD ./app.py
