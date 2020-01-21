#  As it is  demo connector, we will tryout very minimal implimentation concepts
# - Not trying to fix the issue of time out
# - Not optimized connection to support pool or async
# - Not handling isolation level etc ....

import pymysql

class MysqlConnector(object):
    __instance = None
    def __new__(cls, *args, **kwargs):

        if MysqlConnector.__instance is None:
            MysqlConnector.__instance = pymysql.connect(host='localhost', port=3306,
                                                        user='root', passwd='root', db='cricket',
                                                        cursorclass=pymysql.cursors.DictCursor)
        return MysqlConnector.__instance
