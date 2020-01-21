from utils.utils_api_base import RestBase, Processor
from utils.utils_constants import Status


class Top4Winners(RestBase, Processor):

    URL = 'top-winners'

    def process_get(self):
        sql = "SELECT winner FROM matches WHERE season=%s GROUP BY winner ORDER BY COUNT(*) DESC LIMIT 4"
        args = (2014, ) # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict

class Q2(RestBase, Processor):

    URL = 'q2'

    def process_get(self):
        sql = "SELECT toss_winner, COUNT(*) AS total FROM matches WHERE season=%s " \
              "GROUP BY toss_winner ORDER BY total DESC LIMIT 1;"

        args = (2014, ) # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict