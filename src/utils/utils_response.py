import logging
import json
from flask import jsonify
from typing import Dict


logger = logging.getLogger(__name__)


class Response(object):

    @classmethod
    def get(cls, result_dict: Dict, _type=None, message=None, status_code: int = 200):
        from app import app
        if status_code != 200:
            result_dict = {"type": _type, "message": message}
        logger.debug(json.dumps(result_dict, indent=4))
        content = jsonify(result_dict)
        response = app.make_response((content, status_code))
        return response
