# users.py
import cherrypy
import json
from _wine_database import _wine_database

class UserController(object):

    def __init__(self, wdb=None):
        if wdb is None:
            self.wdb = _wine_database()
        else:
            self.wdb = wdb
        self.wdb.load_all('/data/wine_data.csv')
        
    def GET_USER_KEY(self, user_id):
        
        output = {'result' : 'success'}
        user_id = int(user_id)

        try:
            user = self.wdb.get_user(user_id)

            if user is not None:
                output['name'] = user[0]
                output['twitter'] = user[1]
            else:
                output['result'] = 'error'
                output['message'] = 'user not found'
        
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    
    def POST_USER(self):
        temp = list(self.wbd.users)
        uid = max(temp) + 1
        uid = int(uid)
        output = {'result' : 'success'}

        data = json.loads(cherrypy.request.body.read())

        try:
            user = list()
            user.append(data['name'])
            user.append(data['twitter'])
            self.wdb.set_user(uid, user)

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)


    def DELETE_USER_KEY(self, user_id):
        output = {'result' : 'success'}
        user_id = int(user_id)

        try:
            user = self.wdb.delete_user(user_id)
        
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)