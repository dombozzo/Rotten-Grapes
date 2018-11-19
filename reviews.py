import cherrypy    
import json
from _wine_database import _wine_database

class ReviewController(object):
    def __init__(self, wdb=None):
        if wdb is None:
            self.wdb = _wine_database()
        else:
            self.wdb = wdb
        self.wdb.load_all("data/wine_data.csv")

    def GET(self):
        output = {'result': 'success'}

        try:
            data = json.loads(cherrypy.request.body.read().decode())
            wine_info = self.wdb.get_review(data['uid'], data['bid'])
            if wine_info:
                output = {**output, **wine_info}
            else:
                output['result'] = 'error'
                output['message'] = "Review with the specified id's does not exist"
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)

    def DELETE(self):
        output = {'result': 'success'}

        try:
            data = json.loads(cherrypy.request.body.read().decode())
            self.wdb.delete_review(data['uid'], data['bid'])
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)

    def POST(self):
        output = {'result': 'success'}

        try:
            data = json.loads(cherrypy.request.body.read().decode())
            self.wdb.set_review(data['uid'], data['bid'], {'score': data['score'], 'description': data['description']})
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)

    def GET_VID(self, vid):
        output = {'result': 'success'}

        try:
            # Still need to finish
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)