import unittest
import requests
import json

class TestBottles(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:52087' # malir's number
    BOTTLES_URL = SITE_URL + '/bottles/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        b = {}
        r = requests.put(self.RESET_URL, data = json.dumps(b))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_bottles_get(self):
        self.reset_data()
        bottle_id = 28950
        r = requests.get(self.BOTTLES_URL + str(bottle_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        data = resp["information"]
        self.assertEquals(data['title'], 'Citation 2004 Pinot Noir (Oregon)')
        self.assertEquals(data['variety'], 'Pinot Noir')

    def test_bottles_post(self):
        self.reset_data()
        w = {}
        w['title'] = 'Dom'
        w['variety'] = 'likes'
        w['province'] = 'to'
        w['price'] = 95
        w['winery'] = 'make'
        w['designation'] = 'test'
        w['country'] = 'files!'

        r = requests.post(self.BOTTLES_URL, data = json.dumps(w))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        #self.assertEqual(resp['id'], 3953)

        r = requests.get(self.BOTTLES_URL + str(resp['id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode('utf-8'))
        data = resp["information"]
        self.assertEqual(data['title'], w['title'])
        self.assertEqual(data['variety'], w['variety'])


    def test_bottles_delete(self):
        self.reset_data()
        bottle_id = 28950

        w = {}
        r = requests.delete(self.BOTTLES_URL + str(bottle_id), data = json.dumps(w))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.BOTTLES_URL + str(bottle_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')

    def test_bottles_get_all(self):
        self.reset_data()
        r = requests.get(self.BOTTLES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        wines = resp['wines']
        for wine in wines:
            if wine['id'] == 28950:
                testwine = wine

        self.assertEqual(testwine['title'], 'Citation 2004 Pinot Noir (Oregon)')

if __name__ == "__main__":
	unittest.main()
