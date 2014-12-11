
import json
import os
os.environ['DB_PORT_6379_TCP_ADDR'] = 'localhost'
import unittest

import app


class RetwisTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_create_user(self):
        d = json.dumps({'user': {'username': 'niklas9', 'passwd': 'asdf'}})
        rv = self.app.post('/api/v1/users', data=d,
                           content_type='application/json')
        assert rv.status_code == 201

    def test_tweets_get(self):
        rv = self.app.get('/api/v1/tweets')
        assert rv.mimetype == 'application/json'
        try:
            d = json.loads(rv.data)
        except:
            d = None
        assert not d == None
        assert 'tweets' in d
        assert type(d['tweets']) == list


if __name__ == '__main__':
    unittest.main()
