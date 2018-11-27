# users.py
import cherrypy
import json
from _wine_database import _wine_database

class UserController(object):

    def __init__(self, wdb=None):
        if wdb is None:
            self.wdb = _wine_database()
            self.wdb.load_all('data/wine_data.csv')
        else:
            self.wdb = wdb


    def GET_USER_KEY(self, user_id):

        output = {'result' : 'success'}
        user_id = int(user_id)

        try:
            user = self.wdb.get_user(user_id)

            if user is not None:
                output['name'] = user['name']
                output['twitter'] = user['twitter']
            else:
                output['result'] = 'error'
                output['message'] = 'user not found'

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def POST_USER(self):
        uid = max(self.wdb.users.keys()) + 1
        # uid = max(temp) + 1
        # uid = int(uid)
        output = {'result' : 'success'}

        data = json.loads(cherrypy.request.body.read())

        try:
            uinfo = {}
            uinfo['name'] = data['name']
            uinfo['twitter'] = data['twitter']
            self.wdb.set_user(uid, uinfo)

            output['user_id'] = uid

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