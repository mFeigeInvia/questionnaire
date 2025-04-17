# coding=utf-8

# Job A and B should request API source, A should store the result in DestDatabase and B in DestS3
class APISource:
    def __init__(self):
        self.__client = None  # e.g. facebook client

    def get(self) -> list:
        return ['a', 'b', 'c']

class DestDatabase:
    def store_data(self) -> None:
        pass  # no need to be implemented

class DestS3:
    def store_data(self) -> None:
        pass  # no need to be implemented


class JobA:
    pass


class JobB:
    pass
