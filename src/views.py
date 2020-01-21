from utils.utils_api_base import RestBase, Processor
from utils.utils_constants import Status


class Top4Winners(RestBase, Processor):
    URL = 'top-winners'

    def process_get(self):
        sql = "SELECT winner FROM matches WHERE season=%s GROUP BY winner ORDER BY COUNT(*) DESC LIMIT 4"
        args = (2014,)  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict


class Q2(RestBase, Processor):
    URL = 'q2'

    def process_get(self):
        sql = "SELECT toss_winner, COUNT(*) AS total FROM matches WHERE season=%s " \
              "GROUP BY toss_winner ORDER BY total DESC LIMIT 1;"

        args = (2014,)  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict


class Q3(RestBase, Processor):
    URL = 'q3'

    def process_get(self):
        sql = "SELECT player_of_match, COUNT(*) AS max_awards FROM matches " \
              "WHERE season=%s GROUP BY player_of_match order by count(*) DESC LIMIT %s "

        args = (2014, 1)  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict

class Q4(RestBase, Processor):
    URL = 'q4'

    def process_get(self):
        sql = "SELECT  COUNT(*), winner FROM matches group by winner order by count(*) DESC LIMIT %s "

        args = (10, )  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict


class Q5(RestBase, Processor):
    URL = 'q5'

    def process_get(self):
        sql = "SELECT  COUNT(*) AS wins, winner, city FROM matches " \
              "WHERE season=%s GROUP BY winner, city order by wins DESC LIMIT %s"

        args = (2014, 1)  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict


class Q6(RestBase, Processor):
    URL = 'q6'

    def process_get(self):
        sql = "SELECT COUNT(*)/(SELECT COUNT(*) FROM matches  " \
              "WHERE toss_decision='bat') * 100 as per, toss_winner " \
              "FROM matches WHERE season=%s AND toss_decision=%s group by toss_winner order by per desc"

        args = (2014, 'bat', )  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict

class Q7(RestBase, Processor):
    URL = 'q7'

    def process_get(self):
        sql = "SELECT COUNT(*)/(SELECT COUNT(*) FROM matches  " \
              "WHERE toss_decision='bat') * 100 as per, toss_winner " \
              "FROM matches WHERE season=%s AND toss_decision=%s group by toss_winner order by per desc"

        args = (2014, 'bat', )  # IT can going fwd dynamic , get from url param
        result_dict = self.execute(sql, args)
        return Status.SUCCESS, None, None, result_dict