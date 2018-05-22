from simpleLibrary import *


functionLibrary = {}
tokens = ['!', 'WRITE', '+', 'IF', '<', '>']
inPut = []
varDict = {}
isString = False
isInt = False
numList = []
stringList = []
n = {}
log = []
bools = []

def varSetter():
    for chars in tokens:
       # write(i)
        w = words.split('VAR')
        wFuncs = words.split('WRITE')
        #write(wFuncs)
        if chars not in w:
            if '#' or '$' in chars:

                varDict[str(w[0])] = str(w[-1])

    for elements in varDict:
        intOccurs = elements.count('#')

        if '#' in elements:
            numList.append(elements)
            #intSet()


        if '$' in elements:
            stringList.append(elements)
            #stringSet()


    for notVars in varDict:
        n = varDict.copy()

    if 'WRITE' in notVars:
        del varDict[notVars]
                   # write(varDict)


       # write(functionLibrary)
       # write(varDict)

def intSet():
    isString = False
    isInt = True


def stringSet():
    isString = True
    isInt = False

def boolStat():
    # commands for conditional operators

    cond = words.split('!IF(')
    condJoiner = ''.join(cond)
    condJoinerN = condJoiner.split(')!')
    finalCond = ''.join(condJoinerN)

    bools = []

    for chars in finalCond:
        if chars.isdigit() or chars in tokens[:]:

            bools.append(chars)
            if len(bools) > 3:
                bools = []

    numFinal = ''.join(bools)
    lBool = eval(numFinal)

    if lBool:
        write(lBool)
        writeFun = 2 > 1
        execute = words.split('!')
        exJoin = execute[2]
        exFinal = exJoin.split('{')
        exFi = ''.join(exFinal)
        exFinale = exFi.split('}')
        finalExecution = exFinale[0]

        if 'WRITE' in finalExecution:
            writeSequence = finalExecution.split('WRITE')
            writeStringJoin = ''.join(writeSequence)
            fWriteSequence = writeStringJoin.split('(')
            o = ''.join(fWriteSequence)
            fWrite = o.split(')')
            finalWriter = ''.join(fWrite)
            write(finalWriter)
            for everything in varDict:
                if everything in finalWriter:
                    write(varDict[everything])
    else:
        pass



def writing():

    # i likely will rewrite this so that it is more reusable for the entire project
    #  because i find myself repeating this same code with little differences for all functions
    #  within the code.
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



def ui(rawInput):
    global prompt
    global promptVal

    prompt = input(rawInput)

    if prompt:
        promptVal = prompt

        return promptVal + ' (ui)'
    varDict[finalPrompt[1]] = [promptVal]

def uIOut():
    global finalPrompt
    promptSeq = words.split('UI')
    promptJOin = ''.join(promptSeq)
    fPrompt = promptJOin.split('(')
    lPrompt = ''.join(fPrompt)
    fPromptW = lPrompt.split(')')
    finalPrompt = ''.join(fPromptW)

    ui(finalPrompt)


with open('scroll.glif', 'r') as readFile:
    for words in readFile:
        inPut.append(words)

        if '!' in words:
            boolStat()

        if 'VAR' in words:
            varSetter()


        if 'WRITE' in words:
            if '!' not in words:
                writing()
        if 'UI' in words:
            uIOut()