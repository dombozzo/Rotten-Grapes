import cherrypy
import json
from _wine_database import _wine_database

class ReviewController(object):
    def __init__(self, wdb=None):
        if wdb is None:
            self.wdb = _wine_database()
            self.wdb.load_all("data/wine_data.csv")
        else:
            self.wdb = wdb


    # def GET_REVIEW(self):
    #     output = {'result': 'success'}
    #
    #     try:
    #         data = json.loads(cherrypy.request.body.read().decode())
    #         wine_info = self.wdb.get_review(data['uid'], data['bid'])
    #         if wine_info:
    #             output = {**output, **wine_info}
    #         else:
    #             output['result'] = 'error'
    #             output['message'] = "Review with the specified id's does not exist"
    #     except Exception as ex:
    #         output['result'] = 'error'
    #         output['message'] = str(ex)
    #
    #     return json.dumps(output)

    def GET_REVIEW(self, uid, bid):
        output = {'result': 'success'}

        try:
            wine_info = self.wdb.get_review(int(uid), int(bid))
            if wine_info is not None:
                wine_info['score'] = str(wine_info['score'])
                output = {**output, **wine_info}
            else:
                output['result'] = 'error'
                output['message'] = "Review with the specified id's does not exist"
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def DELETE_REVIEW(self, uid, bid):
        output = {'result': 'success'}

        try:
            #data = json.loads(cherrypy.request.body.read().decode())
            self.wdb.delete_review(int(uid), int(bid))
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def POST_REVIEW(self):
        output = {'result': 'success'}

        try:
            data = json.loads(cherrypy.request.body.read().decode())
            self.wdb.set_review(data['uid'], data['bid'], {'score': data['score'], 'description': data['description']})
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_REVIEW_KEY(self, vid):
        output = {'result': 'success'}
        vid = int(vid)

        try:
            variety_info = self.wdb.get_variety_review(vid)
            if variety_info:
                output['data'] = variety_info
            else:
                output['result'] = 'error'
                output['message'] = "No reviews with specified variety found"
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
