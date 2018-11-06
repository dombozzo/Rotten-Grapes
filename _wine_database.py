import numpy as np
import pandas as pd

class _wine_database:

    def __init__(self):
        self.wines = {}
        self.users = {}
        self.reviews = {}

    def load_all(self, movie_file):
        df = pd.read_csv(movie_file)
        df = df.assign(taster_id=(df['taster_name']).astype('category').cat.codes)
        df = df.assign(variety_id=(df['variety']).astype('category').cat.codes)
        df = df.assign(bottle_id=(df['title']).astype('category').cat.codes)
        df = df.drop(['region_1', 'region_2'], axis=1)
        self.reviews = df
        for index, row in df.iterrows():
            if row['taster_id'] not in self.users:
                self.users[row['taster_id']] = {'name': row['taster_name'], 'twitter': row['taster_twitter_handle']}
            if row['bottle_id'] not in self.wines:
                self.wines[row['bottle_id']] = {
                    'title': row['title'],
                    'variety': row['variety'],
                    'province': row['province'],
                    'price': row['price'],
                    'winery': row['winery'],
                    'designation': row['designation'],
                    'country': row['country']
                }

        def get_user(self, uid):
            return self.users.get(uid)

        def get_wine(self, wid):
            return self.wines.get(wid)


if __name__ == '__main__':
    wines = _wine_database()
    wines.load_all('data/wine_data.csv')
