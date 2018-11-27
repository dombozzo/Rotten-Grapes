import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52087'
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        data = resp['result']
        self.assertEquals(data, 'success')

if __name__ == "__main__":
	unittest.main()

