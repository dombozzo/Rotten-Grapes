import cherrypy
import json
from _wine_database import _wine_database

class BottleController(object):

    def __init__(self, wdb = None):
        if wdb is None:
            self.wdb = _wine_database()
        else:
            self.wdb = wdb

        self.wdb.load_all("data/wine_data.csv")

    # GET_ALL
    def GET_BOTTLE(self):
        #return list of all bottles
        output = {'result': 'success'}

        try:
            wines = []
            for key,val in self.wdb.wines.items():
                w = dict()
                w['id'] = key
                w['title'] = val['title']
                w['variety'] = val['variety']
                w['province'] = val['province']
                w['price'] = val['price']
                w['winery'] = val['winery']
                w['designation'] = val['title']
                w['country'] = val['title']
                wines.append(w)
            output['wines'] = wines

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    #GET wid
    def GET_BOTTLE_KEY(self, bid):
        #return info on one bottle
        output = {'result': 'success'}
        bid = int(bid)

        try:
            wine = self.wdb.get_wine(bid)

            if wine is not None:
                output["information"] = wine
            else:
                output['result'] = 'error'
                output['message'] = 'user not found'

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    #POST new bottle
    def POST_BOTTLE(self):
        #add a new bottle. info passed through payload
        data = json.loads(cherrypy.request.body.read())

        #get new id for the bottle
        wid = max(self.wdb.users.keys()) + 1
#         wid = max(temp) + 1
#         wid = int(wid)

        output = {'result' : 'success', 'id' : wid}
        try:
            self.wdb.set_wine(wid, data)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    #DELETE all
    def DELETE_BOTTLE(self):
        #clear all wines
        output = {'result' : 'success'}
        try:
            self.wdb.wines.clear()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    #DELETE wid
    def DELETE_BOTTLE_KEY(self, bid):
        #delete info on one bottle
        output = {'result': 'success'}
        bid = int(bid)

        try:
            wine = self.wdb.delete_wine(bid)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
