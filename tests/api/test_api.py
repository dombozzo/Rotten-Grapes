from _wine_database import _wine_database
import unittest

class TestWineDatabase(unittest.TestCase):

        #@classmethod
        wdb = _wine_database()

        def reset_data(self):
                "reset data is required because we cannot promise an order of test case execution"
                # note that our load_all function clears all data in the system before reloading
                self.wdb.load_all("../../data/wine_data.csv")

        # these tests work already

        def test_get_wine(self):
                self.reset_data()
                wine = self.wdb.get_wine(28950)
                self.assertEquals(wine['title'], 'Citation 2004 Pinot Noir (Oregon)')
                self.assertEquals(wine['variety'], 'Pinot Noir')

        def test_get_wine_null(self):
                self.reset_data()
                wine = self.wdb.get_wine(-1)
                self.assertEquals(wine, None)

        def test_set_wine(self):
                self.reset_data()
                wine = self.wdb.get_wine(28950)
                wine['title'] = 'youve been tested!'
                self.wdb.set_wine(28950, wine)
                wine = self.wdb.get_wine(28950)
                self.assertEquals(wine['title'], 'youve been tested!')

        def test_delete_wine(self):
                self.reset_data()
                self.wdb.delete_wine(28950)
                wine = self.wdb.get_wine(28950)
                self.assertEquals(wine, None)

        def test_get_user(self):
                self.reset_data()
                user = self.wdb.get_user(15)
                self.assertEquals(user['name'], 'Roger Voss')
                self.assertEquals(user['twitter'], '@vossroger')

        def test_set_user(self):
                self.reset_data()
                user = self.wdb.get_user(15)
                user['name'] = 'Mr. Test'
                user['twitter'] = '@mrtesty'
                self.wdb.set_user(15, user)
                user = self.wdb.get_user(15)
                self.assertEquals(user['name'], 'Mr. Test')
                self.assertEquals(user['twitter'], '@mrtesty')

        def test_delete_user(self):
                self.reset_data()
                self.wdb.delete_user(15)
                user = self.wdb.get_user(15)
                self.assertEquals(user, None)

        def test_get_review(self):
                self.reset_data()
                review = self.wdb.get_review(9, 79521)
                score = review['score']
                descrip = review['description']
                self.assertEquals(score, 87)
                self.assertEquals(descrip, "Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")

        def test_get_variety_review(self):
                self.reset_data()
                review = self.wdb.get_variety_review(690)
                self.assertEquals(review['featured_wines'][0]['score'], 97)
                self.assertEquals(review['average_rating'], 87.353)
                self.assertEquals(review['variety'], "White Blend")

        def test_set_review(self):
                self.reset_data()
                review_info = {'score': 76, 'description': 'good stuff'}
                self.wdb.set_review(9, 2058, review_info)

                review = self.wdb.get_review(9, 2058)
                self.assertEquals(review['score'], 76)
                self.assertEquals(review['description'], 'good stuff')

        def test_delete_review(self):
                self.reset_data()
                review_info = {'score': 76, 'description': 'good stuff'}
                self.wdb.set_review(9, 2058, review_info)

                review = self.wdb.get_review(9, 2058)
                self.assertEquals(review['score'], 76)
                self.assertEquals(review['description'], 'good stuff')

                self.wdb.delete_review(9, 2058)
                review = self.wdb.get_review(9, 2058)
                self.assertEquals(review, None)


if __name__ == "__main__":
    unittest.main()
