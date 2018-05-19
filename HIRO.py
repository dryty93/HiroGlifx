from simpleLibrary import *
from HIROTEST import getType

equations = []
fEquationList = []
numList = []
strList = []
isString = 1 > 33
isNum = 1 > 333
VARS = []
NUMS = []
STRINGS = []
indChars = []
symbols = []
addition = []
subtraction = []
varVals = []
fVarName = []
EVAL = ['+', '-', '*', '/']
dataTypes = {"$":"STRING", "#":"NUM"}
varNamesFinal = []
counter = 0
h = []
nub = []
mm = []
tokens = {'!': False,
          'IF': 'if',
          '|?|': 'or',
          '&': 'and',
          '^': 'not',
          'within': 'in',
          'variable':'VAR',
          }

keywords = ['WRITE', 'TYPES']
counter = 1
varDict = {}
with open('HIRO.glif','r') as readFile:

    for words in readFile:

        VARS.append(words)

        if 'WRITE' in words:
            numList = []
            writing()


        def writing():
            writeSequence = words.split('WRITE')
            writeStringJoin = ''.join(writeSequence)
            fWriteSequence = writeStringJoin.split('(')
            o = ''.join(fWriteSequence)
            fWrite = o.split(')')
            finalWriter = ''.join(fWrite)
            write(finalWriter)
            for everything in varDict:
                if everything in finalWriter:
                    write(varDict[everything])


        if '!' in words:
            bool()

        def bool():
            tokens['!'] = True

            if tokens:
                print('conditional')
            else:
                print('no')


        for items in varDict:
            if "#" in items and "WRITE" not in items:
                isString = False
                isNum = True
                numList.append(items)


            if "$" in items:
                isString = True
                isNum = False
                strList.append(items)


        if not isNum:
            nub = []

        for numbers in numList:
           h.append(varDict[numbers])
        for el in h:
            rr = el.join('#=')

        if 'UI' in words:
            def ui(rawInput):

                global e

                prompt = input(rawInput)
                if prompt:
                    promptVal = prompt

                    return promptVal + ' (ui)'

            promptSeq = words.split('UI')
            promptJOin = ''.join(promptSeq)
            fPrompt = promptJOin.split('(')
            lPrompt = ''.join(fPrompt)
            fPromptW = lPrompt.split(')')
            finalPrompt = ''.join(fPromptW)
            ui(finalPrompt)


        counter += 1
        w = words.split('VAR')
        varDict[str(w[0])] = str(w[-1])

        varNames =str(varDict.keys())
        varValues = str(varDict.values())
