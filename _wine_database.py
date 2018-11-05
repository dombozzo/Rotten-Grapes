import numpy as np
import pandas as pd

class _wine_database:

    def __init__(self):
        self.wines = {}
        self.users = {}

    def load_all(self, movie_file):
        df = pd.read_csv(movie_file)
        df = df.assign(taster_id=(df['taster_name']).astype('category').cat.codes)
        df = df.assign(variety_id=(df['variety']).astype('category').cat.codes)
        df = df.assign(title_id=(df['title']).astype('category').cat.codes)
        df = df.drop(['region_1', 'region_2'], axis=1)

if __name__ == '__main__':
    wines = _wine_database()
    wines.load_all('data/wine_data.csv')