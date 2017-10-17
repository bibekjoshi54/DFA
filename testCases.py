import unittest
import dfa

class DFATestCase(unittest.TestCase):
    
    def setUp(self):
        self.alphabets = set(['0','1'])
        self.states = set(['a','b'])
        self.initialState = 'a'
        self.endState = set(list('b'))
        self.transitionRule = {
            ('a','0') : 'b',
            ('a', '1') : 'a',
            ('b','0') : 'b',
            ('b','1'): 'a'
        }
        self.transitionRuleIncomplete = {
            ('a','0') : 'b',
            ('a', '1') : 'a',
            ('b','0') : 'b',
        }
        self.dfaTrue =  dfa.DFA(self.alphabets,self.states,self.initialState,self.endState,self.transitionRule)
        self.dfaFalse = dfa.DFA(self.alphabets,self.states,self.initialState,self.endState, self.transitionRuleIncomplete)

    def testIsDFA(self):
        self.assertTrue(self.dfaTrue.checkDFA())
      

    def testIsNDFA(self):
        self.assertFalse(self.dfaFalse.checkDFA())

    def testResetCurrentState(self):
        self.dfaTrue.resetState()
        self.assertTrue(self.dfaTrue.currentState == None)


    def testSetInitailState(self):
        self.dfaTrue.setInitalState()
        self.assertTrue(self.dfaTrue.currentState == self.initialState)
        self.dfaTrue.resetState()
    
    def testIsFinalState(self):
        self.dfaTrue.currentState = list(self.endState)[0]
        self.assertTrue(self.dfaTrue.checkFinalState())
        self.dfaTrue.resetState()

    def testIsNotFinalState(self):
        self.dfaTrue.currentState = list(self.alphabets.difference(self.endState))[0]
        self.assertFalse(self.dfaTrue.checkFinalState())
        self.dfaTrue.resetState()

    def testIsCorrectString(self):
        self.dfaTrue.inputString = '100100101010'
        self.assertTrue(self.dfaTrue.checkString())

    def testIsNotCorrectString(self):
        self.dfaTrue.inputString = '10a01'
        self.assertFalse(self.dfaTrue.checkString())

    def testStart(self):
        self.assertTrue(self.dfaTrue.start('100'))
        self.assertTrue(self.dfaTrue.start('110'))
        self.assertTrue(self.dfaTrue.start('1110010101010'))
        self.assertTrue(self.dfaTrue.start('100101010100'))
        self.assertFalse(self.dfaTrue.start(''))
        self.assertFalse(self.dfaTrue.start('1'))
        self.assertFalse(self.dfaTrue.start('101'))
        self.assertFalse(self.dfaTrue.start('1001'))
        
        

if __name__ == '__main__':
    unittest.main()
    