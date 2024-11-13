# coding=utf-8

# Job A and B should request API source, A should store the result in Dest1 and B in Dest 2
class APISource:
    def __init__(self):
        self.__client = None

    def get(self) -> list:
        return ['a', 'b', 'c']

class Dest1:
    def store_data(self) -> None:
        pass

class Dest2:
    def store_data(self) -> None:
        pass


class JobA:
    pass


class JobB:
    pass
