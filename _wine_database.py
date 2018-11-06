import numpy as np
import pandas as pd

class _wine_database:

    def __init__(self):
        self.wines = {}
        self.users = {}
        self.reviews = {}

    def load_all(self, movie_file):
        #clear what was present before
        self.wines = {}
        self.users = {}
        self.reviews = {}
        
        #read in new data
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

# TODO
    def get_review(self, uid, wid):
        # TODO. not sure how to access datafram correctly
        # This should just be returning the review information for a given user and wine bottle
        pass
    
#TODO
    def get_variety_review(self, vid):
        # given variety id, iterate through dataframe for ratings of wines in this vid
        # return list of sorted ratings, average rating, or even better: BOTH
        pass

    ####### SETS #######
    def set_user(self, uid, new_user_info):
        # update info for uid if in dictionary, add new element otherwise
        # new_user_info is a dictionary containing 'name' and 'twitter'
        self.users[uid] = new_user_info

    def set_wine(self, wid, new_wine_info):
        # update info for uid if in dictionary, add new element otherwise
        # new_wine_info is a dictionary containing all required elements for wine
        self.wines[wid] = new_wine_info
#TODO
    def set_review(self, uid, wid, review_info):
        # add element to the datafram if this review isn't present
        # we can assume that review_info has a dictionary of 'description', 'rating'
        # add whatever else we need to set
        pass

    ####### DELETES #######
    def delete_user(self, uid):
        del self.users[uid]
#TODO
    def delete_wine(self, wid):
        #TODO: should we delete all reviews mentioning this wine at this point too?
        del self.wines[wid]

#TODO
    def delete_review(self, uid, wid):
        # TODO. delete proper row of the dataframe
        pass


        def get_user(self, uid):
            return self.users.get(uid)

        def get_wine(self, wid):
            return self.wines.get(wid)


if __name__ == '__main__':
    wines = _wine_database()
    wines.load_all('data/wine_data.csv')
