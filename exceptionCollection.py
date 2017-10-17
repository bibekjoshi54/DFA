
class Error(Exception):
    pass


class StringError(Error):
    
    def __init__(self, expression, message='The input string have invalid alphabet'):
        self.expression = expression
        self.message = message


class NDFAError(Error):

    def __init__(self,transitionRule, message='Given FA is not DFA'):
        self.transitionRule = transitionRule
        self.message = message