import parser
import dfa
import sys
import exceptionCollection

def takeInput():
    string = input('> ')
    if string:
        if string == 'exit()':
            exit(0)
    else:
        string = ''
    return string

def main():
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = input('Enter the program Name: ')
    userParser = parser.Parser(fileName)
    userParser.format()
    try:
        userDfa = dfa.DFA(userParser.dfaValues[0],userParser.dfaValues[1],userParser.dfaValues[2],userParser.dfaValues[3],userParser.dfaValues[4])
    except:
        exit('Syntax Error Ocuured')
    print('Your DFA has been loaded to the shell.')
    string = takeInput()
    while len(string) >= 0:
        try:
            print(userDfa.start(string))
        except exceptionCollection.StringError:
            print('Please enter the valid string')
        string = takeInput()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram Ended')