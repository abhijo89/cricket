import enum


@enum.unique
class Status(enum.Enum):

    SUCCESS = 'success'
    FAILURE = 'failure'
