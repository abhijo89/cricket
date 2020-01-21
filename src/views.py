from utils.utils_api_base import RestBase
from utils.utils_connector import MysqlConnector
from utils.utils_constants import Status


class Top4Winners(RestBase):

    URL = 'top-winners'

    def process_get(self):
        conn = MysqlConnector()
        cursor = conn.cursor()
        cursor.execute("SELECT winner FROM matches WHERE season=2014 GROUP BY winner ORDER BY COUNT(*) DESC LIMIT 4;")
        result_dict = cursor.fetchall()
        return Status.SUCCESS, None, None, result_dict
