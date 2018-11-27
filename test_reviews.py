import unittest
import requests
import json

class TestBottles(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:52087' # malir's number
    REVIEWS_URL = SITE_URL + '/reviews/'
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

    def test_reviews_get(self):
        self.reset_data()
        bottle_id = 79521
        r = requests.get(self.REVIEWS_URL + str(bottle_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        data = resp['info']
        self.assertEquals(data['description'], "Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")
        self.assertEquals(data['score'], 87)

        # review = self.wdb.get_review(9, 79521)
        # score = review['score']
        # descrip = review['description']
        # self.assertEquals(score, 87)
        # self.assertEquals(descrip, "Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")



if __name__ == "__main__":
	unittest.main()
