# Matthew J. Malir
# CherryPy Project
# 12 November 2018

import json, re
import cherrypy

from _wine_database import _wine_database

class ResetController(object):
    def __init__(self, wdb = None):
        if wdb is None:
            self.wdb = _wine_database()
        else:
            self.wdb = wdb

    # event handlers for /reset/ requests
    def PUT_RESET(self):
        output = {'result': 'success'}

        try:
            # reload all data
            self.wdb.load_all('data/wine_data.csv')
        except Exception as ex:
            output['result'] = 'error'
            output['message']  = str(ex)

        return json.dumps(output)