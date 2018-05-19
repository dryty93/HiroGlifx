from simpleLibrary import *
from HIRO_HELPER import getType

bools = []
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
fVarName = []
EVAL = ['+', '-', '*', '/']
dataTypes = {"$":"STRING", "#":"NUM"}
varNamesFinal = []
counter = 0
h = []
promptList = []
tokens = ['!','!IF', '$','#', '&', '<','>','=','!=']

keywords = ['WRITE', 'TYPES']
counter = 1
varDict = {}

with open('scroll.glif','r') as readFile:

    for words in readFile:

        VARS.append(words)
        if '!IF' in words:
            cond = words.split('!IF(')
            condJoiner = ''.join(cond)
            condJoinerN = condJoiner.split(')!')
            finalCond = ''.join(condJoinerN)
            for chars in finalCond:
                if chars.isdigit() or chars in tokens[:]:
                    bools.append(chars)
            numFinal = ''.join(bools)
            lBool = eval(numFinal)
            



        if 'WRITE' in words:
            numList = []
            writing()



        def writing():

            #i likely will rewrite this so that it is more reusable for the entire project.
            #because i find myself repeating this same code with little differences for all functions
            # within the code.
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



        for items in varDict:
            if "#" in items and "WRITE" not in items:
                isString = False
                isNum = True
                numList.append(items)

            if "+" in varValues and isString == False:
                addThis = varDict[items].split('=')
                add = addThis[1]
                added = add.split('+')


            if "$" in items and 'WRITE' not in items:
                isString = True
                isNum = False
                strList.append(items)

            if "^" in items and 'WRITE' not in items:
                promptList.append(promptVal)

        for numbers in numList:
           h.append(varDict[numbers])

        if 'UI' in words:

            def ui(rawInput):

                global promptVal

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
            varDict[finalPrompt[1]] = [promptVal]


        counter += 1
        w = words.split('VAR')
        varDict[str(w[0])] = str(w[-1])

        varNames =str(varDict.keys())
        varValues = str(varDict.values())
