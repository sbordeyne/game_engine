class EngineException(Exception):
    def __init__(self, message=""):
        self.type = type(self).__name__
        self.message = message

    def __str__(self):
        return f"{self.type} : {self.message}"

    def __repr__(self):
        return self.__str__()
