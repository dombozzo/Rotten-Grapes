# rotton grapes
import cherrypy
import json

from reviews import ReviewController
from bottles import BottleController
from users import UserController
from reset import ResetController

from _wine_database import _wine_database

# class optionsController:
#     def OPTIONS(self,*args,**kwargs):
#         return ""
#
# def CORS():
#     cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
#     cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
#     cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def start_service():
    # instantiate database
    wdb_o = _wine_database()

    # create controllers
    bottleController = BottleController(wdb = wdb_o)
    reviewController = ReviewController(wdb = wdb_o)
    userController = UserController(wdb = wdb_o)

    # create dispatcher
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # BOTTLES
    # /bottles/
    dispatcher.connect('bottle_get','/bottles/',
        controller = bottleController, action = 'GET_BOTTLE',
        conditions = dict(method = ['GET']))
    dispatcher.connect('bottle_post','/bottles/',
        controller = bottleController, action = 'POST_BOTTLE',
        conditions = dict(method = ['POST']))
    dispatcher.connect('bottle_delete','/bottles/',
        controller = bottleController, action = 'DELETE_BOTTLE',
        conditions = dict(method = ['DELETE']))
    # /bottles/:key
    dispatcher.connect('bottle_get_key','/bottles/:key',
        controller = bottleController, action = 'GET_BOTTLE_KEY',
        conditions = dict(method = ['GET']))
    dispatcher.connect('bottle_delete_key','/bottles/:key',
        controller = bottleController, action = 'DELETE_BOTTLE_KEY',
        conditions = dict(method = ['DELETE']))

    # USERS
    # /users/
    dispatcher.connect('user_post','/users/',
        controller = userController, action = 'POST_USER',
        conditions = dict(method = ['POST']))
    # /users/:key
    dispatcher.connect('user_get_key','/users/:key',
        controller = userController, action = 'GET_USER_KEY',
        conditions = dict(method = ['GET']))
    dispatcher.connect('user_delete_key','/users/:key',
        controller = userController, action = 'DELETE_USER_KEY',
        conditions = dict(method = ['DELETE']))

    # REVIEWS
    # /reviews/
    dispatcher.connect('review_get','/reviews/',
        controller = reviewController, action = 'GET_REVIEW',
        conditions = dict(method = ['GET']))
    dispatcher.connect('review_post','/reviews/',
        controller = reviewController, action = 'POST_REVIEW',
        conditions = dict(method = ['POST']))
    dispatcher.connect('reivew_put','/reviews/',
        controller = reviewController, action = 'PUT_REVIEW',
        conditions = dict(method = ['PUT']))
    dispatcher.connect('review_delete','/reviews/',
        controller = reviewController, action = 'DELETE_REVIEW',
        conditions = dict(method = ['DELETE']))
    # /reviews/:key
    dispatcher.connect('review_get_key','/reviews/:key',
        controller = reviewController, action = 'GET_REVIEW_KEY',
        conditions = dict(method = ['GET']))

    # RESET
    # /reset/
    dispatcher.connect('reset_put','/reset/',
        controller = resetController, action = 'PUT_RESET',
        conditions = dict(method = ['PUT']))

    # configuration for server
    conf = {
            'global': {
                'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': 52087  # malir's port #
               },
            '/': {
                'request.dispatch': dispatcher
                # 'tools.CORS.on': True
                 }
           }

    # update config & start event loop
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    # need to put some CORS thing in here
    start_service()








