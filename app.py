#!/usr/bin/python

import flask
import os
import redis


app = flask.Flask(__name__)
r = redis.Redis(os.environ['DB_PORT_6379_TCP_ADDR'], port=6379)

@app.route('/api/v1/tweets')
def tweets():
    return flask.jsonify({'tweets':[{'text': 'asdf fdsa hugh'}]})

# NOTE(niklas9):
# * index could and should be served by something more optimized than Flask,
#   it's just a static index.html file (Ember.js app)
@app.route('/')
def index():
    if not r.get('counter'):
        r.set('counter', 0)
    r.incr('counter')
    return 'Hey! Current visits - %s\n' % r.get('counter')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
