from simpleLibrary import *


VARS = []
NUMS = []
STRINGS = []
indChars = []
symbols = []
addition = []
subtraction = []
varVals = []
fVarNamesList = []
EVAL = ['+', '-', '*', '/']
varNamesFinal = []
counter = 0
h = []
tokens = {'!': False,
          'IF': 'if',
          '|?|': 'or',
          '&': 'and',
          '^': 'not',
          'within': 'in',
          'variable':'VAR',
          }

keywords = ['WRITE', 'TYPES']

with open('HIRO.glif','r') as readFile:
    
    for words in readFile:
        counter += 1
        w = words.join('#=')
        if w in words:
            nw = words.split(-3)
            
            write(nw)
        else:
            write('do better stupid')

#open file and read it. if any of the words in file match token perform function
#save var names and vals as dictionary to call each of them.













