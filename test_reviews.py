import unittest
import requests
import json

class TestReviews(unittest.TestCase):

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
        uid = 9
        bid = 79521
        r = requests.get(self.REVIEWS_URL + str(uid) + '/' + str(bid))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        review = json.loads(r.content.decode('utf-8'))
        print(review)
        score = review['score']
        descrip = review['description']
        self.assertEquals(score, '87')
        self.assertEquals(descrip, "Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")

    def test_reviews_get_var(self):
        self.reset_data()
        var_id = 690
        r = requests.get(self.REVIEWS_URL + str(var_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        data = resp['data']

        self.assertEquals(data['featured_wines'][0]['score'], 97)
        self.assertEquals(data['average_rating'], 87.35296610169492)
        self.assertEquals(data['variety'], "White Blend")

    def test_reviews_post(self):
        self.reset_data()

        review_info = {'uid': 9 , 'bid' : 2058, 'score': 76, 'description': 'good stuff'}
        r = requests.post(self.REVIEWS_URL, data = json.dumps(review_info))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        data = json.loads(r.content.decode('utf-8'))
        self.assertEquals(data['result'], "success")

        r = requests.get(self.REVIEWS_URL + str(9) + '/' + str(2058))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        review = json.loads(r.content.decode('utf-8'))

        score = review['score']
        descrip = review['description']
        self.assertEquals(score, '76')
        self.assertEquals(descrip, 'good stuff')

    def test_reviews_delete(self):
        self.reset_data()
        # data = {}
        # data['uid'] = 9
        # data['bid'] = 79521
        uid = 9
        bid = 79521
        r = requests.delete(self.REVIEWS_URL + str(uid) + '/' + str(bid))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.REVIEWS_URL + str(uid) + '/' + str(bid))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')


if __name__ == "__main__":
	unittest.main()
