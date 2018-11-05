import numpy as np
import pandas as pd

class _wine_database:

    def __init__(self):
        self.wines = {}
        self.users = {}
        self.ratings = {}

    def load_all(self, movie_file):
        df = pd.read_csv(movie_file)
        df['taster_id'] = df.groupby(['taster_name']).ngroup()
        df['variety_id'] = df.groupby(['variety']).ngroup()
        df['title_id'] = df.groupby(['title']).ngroup()
        '''f = open(movie_file)
        for line in f:
            line = line.strip()
            components = line.split(",")
            # handle empty data entries. for now just replaced with NA
            for i, component in enumerate(components):
                if component == "":
                    components[i] == "Not Available"
        
            #sort into wines, users, and ratings
            num = components[0]
            country = components[1]
            description = components[2]
            designation = components[3]
            points = components[4]
            price = components[5]
            province = components[6]
            region_1 = components[7]
            region_2 = components[8]
            taster = components[9]
            twitter = components[10]
            title = components[11]
            variety = components[12]
            winery = components[13]
            pass

        pass'''

if __name__ == '__main__':
    wines = _wine_database()
    wines.load_all('data/wine_data.csv')