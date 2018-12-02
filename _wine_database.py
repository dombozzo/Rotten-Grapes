import numpy as np
import pandas as pd
import math

class _wine_database:

    def __init__(self):
        self.wines = {}
        self.users = {}
        self.reviews = {}

    def load_all(self, wine_file):
        #clear what was present before
        self.wines = {}
        self.users = {}
        self.reviews = {}

        #read in new data
        df = pd.read_csv(wine_file, index_col=0)
        df = df.assign(taster_id=(df['taster_name']).astype('category').cat.codes)
        df = df.assign(variety_id=(df['variety']).astype('category').cat.codes)
        df = df.assign(bottle_id=(df['title']).astype('category').cat.codes)
        df = df.drop(['region_1', 'region_2'], axis=1)
        self.reviews = df
        for index, row in df.iterrows():
            if row['taster_id'] not in self.users:
                twit = str(row['taster_twitter_handle'])
                if len(twit):
                    twit = "n/a"
                self.users[row['taster_id']] = {'name': row['taster_name'], 'twitter': twit}
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


    ####### GETS #######
    def get_user(self, uid):
        # attemp to return user id info, if not, return None to indicate error
        try:
            return self.users[uid]
        except:
            return None

    def get_wine(self, wid):
        # attemp to return bottle id info, if not, return None to indicate error
        try:
            return self.wines[wid]
        except:
            return None


    def get_review(self, uid, wid):
        # This should just be returning the review information for a given user and wine bottle
        try:
            b1 = self.reviews['taster_id'] == uid
            b2 = self.reviews['bottle_id'] == wid
            review = self.reviews[b1 & b2]
            info = {"score": review['points'].values[0], "description": review['description'].values[0]}
        except :
            return None
        return info

    def get_variety_review(self, vid):
        # given variety id, iterate through dataframe for ratings of wines in this vid
        # return list of sorted ratings, average rating, or even better: BOTH
        try:
            b1 = self.reviews['variety_id'] == vid
            var = self.reviews[self.reviews['variety_id'] == vid].sort_values(by = "points", ascending = False)

            wines = []
            for index, row in var.iterrows():
                title = row['title']
                score = row['points']
                descr = row['description']
                id = row['bottle_id']
                wines.append({"title": title, "score": score, "description": descr, "id": id})


            myd = {
                "variety": var['variety'].values[0],
                "average_rating": np.mean(var['points']),
                "featured_wines": wines
            }
            return myd
        except:
            return None

    def get_variety(self, wid):
        try:
            entries = self.reviews[self.reviews['bottle_id'] == wid]
            vid = entries['variety_id'].values[0]
            return vid
        except:
            return None


    ####### SETS #######
    def set_user(self, uid, new_user_info):
        # update info for uid if in dictionary, add new element otherwise
        # new_user_info is a dictionary containing 'name' and 'twitter'
        self.users[uid] = new_user_info

    def set_wine(self, wid, new_wine_info):
        # update info for uid if in dictionary, add new element otherwise
        # new_wine_info is a dictionary containing all required elements for wine
        self.wines[wid] = new_wine_info

    def set_review(self, uid, wid, review_info):
        # add element to the dataframe if this review isn't present
        # we can assume that review_info has a dictionary of 'description', 'rating'
        # add whatever else we need to set
        # review info is {"score" : 91, "description": "good stuff"}

        #variety_id, bottle_id, and taster_id
        new_entry = {}
        try:
            user_info = self.users[uid]
            wine_info = self.wines[wid]
        except:
            return None

        new_entry['taster_id'] = uid
        new_entry['bottle_id'] = wid
        new_entry['variety_id'] = self.get_variety(wid)
        new_entry['title'] = wine_info['title']
        new_entry['variety'] = wine_info['variety']
        new_entry['province'] = wine_info['province']
        new_entry['price'] = wine_info['price']
        new_entry['winery'] = wine_info['winery']
        new_entry['designation'] = wine_info['designation']
        new_entry['country'] = wine_info['country']

        new_entry['taster_name'] = user_info['name']
        new_entry['taster_twitter_handle'] = user_info['twitter']

        new_entry['points'] = review_info['score']
        new_entry['description'] = review_info['description']

        self.reviews = self.reviews.append(new_entry,ignore_index = True)

    ####### DELETES #######
    def delete_user(self, uid):
        del self.users[uid]
        # delete all user entries in reviews as well
        self.reviews = self.reviews[self.reviews['taster_id'] != uid]

    def delete_wine(self, wid):
        del self.wines[wid]
        #delete all wine reviews as well
        self.reviews = self.reviews[self.reviews['bottle_id'] != wid]

    def delete_review(self, uid, wid):
        b1 = self.reviews['taster_id'] != uid
        b2 = self.reviews['bottle_id'] != wid
        self.reviews = self.reviews[b1 | b2]


if __name__ == '__main__':
    wines = _wine_database()
    wines.load_all('data/wine_data.csv')
    # wines.get_variety_review(690)
    # wines.delete_review(9, 79521)
