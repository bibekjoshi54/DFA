
class Parser(object):
    def __init__(self,fileName):
        self.fileName = fileName
        self.dfaRawValues = None
        self.dfaValues = None
        self.alphabets = None
        self.state = None
        self.initialState = None
        self.finalStates = None
        self.transitionRule = dict() 
        self.dfaRawValues = None     
        self.dfaValues = None
        self.open()                  
        

    def open(self):
        dfaValues = open(self.fileName,'r')
        self.dfaRawValues = dfaValues.read()
        dfaValues.close()
        return self.dfaRawValues

    def format(self):
        self.dfaValues = self.dfaRawValues.split('\n')
        self.alphabets = set(self.dfaValues[0].split(' '))
        self.states = set(self.dfaValues[1].split(' '))
        self.initialState = self.dfaValues[2]
        self.finalStates = set(self.dfaValues[3].split(' '))
        for i in self.dfaValues[4:]:
            i = i.split(' ')
            self.transitionRule[(i[0],i[1])] = i[2]
        self.dfaValues = (self.alphabets, self.states, self.initialState, self.finalStates, self.transitionRule)
        return self.dfaValues

    

        

        

if __name__ == '__main__':
    parser = Parser('ParserTest.txt')
    parser.open()
    a = parser.format()    
    print(a)