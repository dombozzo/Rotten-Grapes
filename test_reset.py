import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52087'
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL)

if __name__ == "__main__":
	unittest.main()

