import unittest
import requests
import json

class TestUsers(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:52087' # replace this with your port number
    USERS_URL = SITE_URL + '/users/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        u = {}
        r = requests.put(self.RESET_URL, data = json.dumps(u))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_users_get(self):
        self.reset_data()
        user_id = 15
        r = requests.get(self.USERS_URL + str(user_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Roger Voss')
        self.assertEqual(resp['twitter'], '@vossroger')

    def test_users_delete(self):
    	self.reset_data()
    	user_id = 15

    	u = {}
    	r = requests.delete(self.USERS_URL + str(user_id), data = json.dumps(u))
    	self.assertTrue(self.is_json(r.content.decode('utf-8')))
    	resp = json.loads(r.content.decode('utf-8'))
    	self.assertEqual(resp['result'], 'success')

    	r = requests.get(self.USERS_URL + str(user_id))
    	self.assertTrue(self.is_json(r.content.decode('utf-8')))
    	resp = json.loads(r.content.decode('utf-8'))
    	self.assertEqual(resp['result'], 'error')

    def test_users_index_post(self):
        self.reset_data()
        u = {}
        u['name'] = 'Matt Malir'
        u['twitter'] = '@mmalir'

        r = requests.post(self.USERS_URL, data = json.dumps(u))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.USERS_URL + str(resp['user_id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], u['name'])
        self.assertEqual(resp['twitter'], u['twitter'])

if __name__ == "__main__":
    unittest.main()

