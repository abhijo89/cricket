#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import logging
from abc import abstractmethod
from typing import Tuple

from flask import Flask
from flask.views import MethodView

from utils.utils_constants import Status
from utils.utils_response import Response
from utils.utils_connector import MysqlConnector

logger = logging.getLogger(__name__)


class Processor(object):

    def __init__(self):
        self.__conn = MysqlConnector()

    @property
    def connection(self):
        # Can check if connctionis closed or not .
        return self.__conn

    def execute(self, query: str, args=None):
        if args is None:
            args = ()
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        result_dict = cursor.fetchall()
        return result_dict


class RestBase(MethodView):
    def __init__(self):
        # As it a demo, Not interested in connection timeout or any other DB related issues
        super().__init__()

    def get(self) -> Flask.make_response:

        status = self.__validate_mandatory_parameters()
        if status == Status.FAILURE.value:
            return Response.get(_type='_type', message='message', status_code=412)
        try:
            status, _type, message, result_dict = self.process_get()
            # Based on status code, You can send any response to the end point
            # Example :
            #   - if status is failure send message and type to the end point
            # Response.get(_type=_type, message='message, status_code=400)
        except Exception as e:
            raise e
            logger.error(f"OH no!!, We got few works for developers, try to figure out {e}")
            return Response.get({}, _type='Unknown Error', message='Some abacd msg', status_code=500)
        return Response.get(result_dict)

    # @abstractmethod
    def process_post(self, *args: str, **kwargs: str) -> Tuple[str, dict]:
        return Status.FAILURE.value, {}

    @abstractmethod
    def process_get(self):
        return Status.FAILURE, '', '', {}

    def __validate_mandatory_parameters(self) -> Tuple[str, str]:
        # Validate the mandatory params, if need in the the views
        return Status.SUCCESS.value, "Validate mandatory successful."

    @property
    @abstractmethod
    def json_schema(self):
        # Used for validating POST data. not implementing for now !! :D
        return self.__json_schema

    def validate_schema(self):
        if inspect.ismethod(self.json_schema):
            raise Exception(f"Should define '{self.json_schema.__name__}' as property")

        # json_schema abstract property is not implimented :D :D
        # Use jsonSchema to validate the post params
        return Status.SUCCESS, None, None

    @property
    def post_data(self):
        return self._request

    def post(self, *args, **kwargs):
        # the same way we implemented GET we can implement POS Also. For now ignoring code, as i am not using it.
        return Response.get({})
