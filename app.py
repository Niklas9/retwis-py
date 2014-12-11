#!/usr/bin/python

import flask
import os
import redis


API_BASE_URL = '/api/v1'

app = flask.Flask(__name__)
r = redis.Redis(os.environ['DB_PORT_6379_TCP_ADDR'], port=6379)

@app.route('%s/users' % API_BASE_URL, methods=['GET'])
def users():
    users = []
    return flask.jsonify({'users': users})

@app.route('%s/users' % API_BASE_URL, methods=['POST'])
def users_create():
    d = flask.request.stream.read()
    try:
        d = flask.json.loads(d)
    except ValueError, e:
        return 'invalid json, <%s>' % e, 400
    if 'user' in d and 'username' in d['user'] and 'passwd' in d['user']:
        return 'asdf==%s' % d, 201
    else:
        return 'missing user fields', 400


@app.route('%s/tweets' % API_BASE_URL, methods=['GET'])
def tweets():
    tweets = [{'id': 1,
               'text': 'Hello fuckface',
               'user': 'niklas9',
               'createdAt': '2014-12-07 15:50:00'},
              {'id': 2,
               'text': 'Spritzen ja',
               'user': 'niklas9',
               'createdAt': '2014-12-09 23:53:22'}]
    return flask.jsonify({'tweets': tweets})

@app.route('%s/tweets' % API_BASE_URL, methods=['POST'])
def tweets_create():
    tweet = {'id': 2, 'text': 'fdsa', 'user': 'neuner',
             'createdAt': '2014-12-08 17:14:33'}
    return flask.jsonify({'tweet': tweet})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
