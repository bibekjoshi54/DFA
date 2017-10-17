import unittest
import parser

class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.alphabets = set(['0', '1'])
        self.states = set(['a', 'b'])
        self.startState = 'a'
        self.finalState = set(['b'])
        self.transition = self.transitionRule = {
            ('a','0') : 'b',
            ('b', '0') : 'b',
            ('a','1') : 'a',
            ('b','1'): 'a'
        }
        self.fileContent = "0 1\na b\na\nb\na 0 b\nb 0 b\na 1 a\nb 1 a"
        self.testFileName = 'ParserTest.txt'
        self.Create()
        self.parser =  self.parser = parser.Parser(self.testFileName)
    
    def testFormat(self):
        self.dfaValues = self.parser.format()
        self.assertFalse(self.dfaValues[0] - self.alphabets)
        self.assertFalse(self.alphabets - self.dfaValues[0])
        self.assertFalse(self.dfaValues[1] - self.states)
        self.assertFalse(self.states - self.dfaValues[1])
        self.assertFalse(set(self.dfaValues[2]) - set(self.startState))
        self.assertFalse(self.dfaValues[3] - self.finalState)
        self.assertFalse(self.finalState - self.dfaValues[3])
        for key in self.dfaValues[4]:
            try:
                self.transition[key]
                self.assertTrue(True)
            except KeyError:
                self.assertTrue(False)
        for key in self.transition:
            try:
                self.dfaValues[4][key]
                self.assertTrue(True)
            except KeyError:
                self.asserTrue(False)
    
    def testOpen(self):
        self.assertTrue(self.parser.open() == self.fileContent)

    def Create(self):
        ab = open(self.testFileName, mode='w')
        ab.write(self.fileContent)
        ab.close()


if __name__ == '__main__':
    unittest.main()
    