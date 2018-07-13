from simpleLibrary import *
from random import randrange
functionLibrary = {}
tokens = ['!', 'WRITE', '+', '!IF', 'ELSE', '<', '>', '@INSIDE@', 'VAR',]
expression = ['+', '-', '/', '*']
inPut = []
varDict = {}
isString = False
isInt = False
numList = []
stringList = []
n = {}
bools = []

def boolSep(string):
    """This seperates booleans based on < or >"""
    stringSplitL = string.split('<')
    stringSplitR = string.split('>')
    stringSplitLJoint = stringSplitL[0]
    stringSplitRJoint = stringSplitR[0]


def varSetter():
    global w
    global insideFunction


    for chars in tokens:
        w = words.split('VAR')
        wFuncs = words.split('WRITE')
        insideFunction = words.split('@INSIDE@')
        n = ' '.join(w)
        rawValFunct = n.split('(')

        if chars not in w:
            if '#' or '$' or '^' in chars:
                varDict[str(w[0])] = str(w[-1])


    for elements in varDict:
        intOccurs = elements.count('#')

        if '#' in elements:
            numList.append(elements)
            intSet()

        if '$' in elements:
            stringList.append(elements)
            # stringSet()

    for notVars in varDict:
        n = varDict.copy()



def intSet():
    global opNow
    global finalOp
    global summ

    isString = False
    isInt = True

    # might have to write seperate functions for each type of problem(add,subtract, etc)
    if '+' in words:
        operation = words.split('=')
        join = ''.join(operation)
        opNow = join.split('#')
        finalOp = opNow[2]
        summ = eval(finalOp)
        varDict[str(w[0])] = summ

    if '-' in words:
        operation = words.split('=')
        join = ''.join(operation)
        opNow = join.split('#')
        finalOp = opNow[2]
        diff = eval(finalOp)
        varDict[str(w[0])] = diff

    if '/' in words:
        operation = words.split('=')
        join = ''.join(operation)
        opNow = join.split('#')
        finalOp = opNow[2]
        quotient = eval(finalOp)
        varDict[str(w[0])] = quotient

    if '*' in words:
        operation = words.split('=')
        join = ''.join(operation)
        opNow = join.split('#')
        finalOp = opNow[2]
        product = eval(finalOp)
        varDict[str(w[0])] = product



def stringSet():
    isString = True
    isInt = False


def comment():
    if not '//' in words:
        pass

    pass


def RANDOM():
    if 'RAND5' in words:
        randomVar = str(randrange(1,5))
    varDict[str(w[0])] = randomVar

    if 'RAND10' in words:
        varDict[str(w[0])] = str(randrange(1, 10))
    elif 'RAND100' in words:
        varDict[str(w[0])] = str(randrange(1, 100))




def boolStat():
    # commands for conditional operators
    global lBool
    global finalCond
    global finalExecution
    bools = []


    cond = words.split('!IF(')
    condJoiner = ''.join(cond)
    condJoinerN = condJoiner.split(')!')
    finalCond = ''.join(condJoinerN)



    if '<BRK>' not in finalCond:

        if 'VAR' and '<' in finalCond or 'VAR' and '>' in finalCond:
            lBoolSplitL = finalCond.split('<')
            lBoolSplitR = finalCond.split('>')
            lBoolSplitLJoint = lBoolSplitL[0]
            lBoolSplitRJoint = lBoolSplitR[0]


            for everything in varDict:
                if everything in lBoolSplitLJoint:
                    convertedKey = str(varDict[everything])
                    finalConvertedKey = convertedKey.split(' ')
                    finalConversionKey = ('').join(finalConvertedKey)
                    finalConvKeyReady = finalConversionKey.split("\n")
                    digAloneKey = ('').join(finalConvKeyReady[0])
                    digAloneFinalkey = digAloneKey.split('=')
                    digKeyF = ('').join(digAloneFinalkey)
                    if '#' in digKeyF:
                        lastConvKey = digKeyF.split('#')
                        digitKey = lastConvKey[1]
                        bools.append(digitKey)

                    elif digKeyF.isdigit():

                        bools.append(digKeyF)


                elif everything in lBoolSplitRJoint:

                    convertedKey = str(varDict[everything])
                    finalConvertedKey = convertedKey.split(' ')
                    finalConversionKey = ('').join(finalConvertedKey)
                    finalConvKeyReady = finalConversionKey.split("\n")
                    digAloneKey = ('').join(finalConvKeyReady[0])
                    digAloneFinalkey = digAloneKey.split('=')
                    digKeyF = ('').join(digAloneFinalkey)


                    if '#' in digKeyF:
                        lastConvKey = digKeyF.split('#')
                        digitKey = lastConvKey[1]
                        bools.append(digitKey)



    for chars in finalCond:
        # put chars for digits as its own list and check the length
        # of the character.
        if chars.isdigit() or chars in tokens:

            bools.append(chars)


    boolDecide = ''.join(bools)
    bareBoolDecide = boolDecide.split('<')
    boolJoin = ''.join(bareBoolDecide)
    bBoolDecideFin = boolJoin.split('>')
    boolFinDecider = ''.join(bBoolDecideFin)

    if boolFinDecider.isdigit():
        numFinal = boolDecide
        # this is supposed to check if the last char is a parenthesis
        if numFinal[-1] in tokens or numFinal[-1] == ' ':

            pass

        else:

            lBool = eval(numFinal)
            if lBool:
                boolExec()


    elif '@INSIDE@' in finalCond:
        bools.append(chars)
        if '\n' in bools:
            bools = []
            if 'VAR' not in finalCond:
                lBoolSplitter = finalCond.split(' ')
                lBoolcond_one = lBoolSplitter[1]
                lBoolcond_two = lBoolSplitter[3]


                if lBoolcond_one in lBoolcond_two:

                    lBool = 2 > 1
                    if lBool:
                        boolExec()

            if 'VAR' in finalCond:
                lBoolSplit = finalCond.split(' @INSIDE@')
                lBoolcond_one = lBoolSplit[0]
                lBoolcond_two_gen = lBoolSplit[1].split('{')
                lBoolcond_two = lBoolcond_two_gen[0]

                # needed so python recognizes var keys
                for everything in varDict:
                    everyString = everything.split('VAR $')

                    if everyString[0] in lBoolcond_one:
                        stringCutter = str(varDict[everything]).split('=')
                        stringJointL = stringCutter[-1].split('\n')

                        if stringJointL[0] in lBoolcond_two:
                            lBool = 2 > 1
                            if lBool:
                                boolExec()


                    if everyString[0] in lBoolcond_two:
                        stringCutter = str(varDict[everything]).split('=')
                        stringJoint = stringCutter[-1].split('\n')
                        if  stringJointL[0] in stringJoint[0]:
                            lBool = 2 > 1
                            if lBool:
                                boolExec()


def boolExec():

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

    if '<BRK>' in finalExecution:

        breakSeq = finalExecution.split('<BRK>')
        breakJoin = ''.join(breakSeq)
        fBreakSeq = breakJoin.split('(')
        b = ''.join(fBreakSeq)
        fbreak = b.split(')')
        finalBreak = ''.join(fbreak)
        exit()

    if '@INSIDE@' in finalExecution:
        insideSeq = finalExecution.split('@INSIDE@')
        insideJoin = ''.join(insideSeq)
        fInsideSeq = insideJoin.split('(')
        r = ''.join(fInsideSeq)
        fSeq = r.split(')')
        finalSeq = ''.join(fSeq)
        write(finalSeq)
        for everything in varDict:
            if everything in finalSeq:
                varDict[everything]

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

    for everything in varDict.keys():
        if everything in finalWriter:
            write(varDict[everything])

def ui(userInput):
    global prompt
    global promptVal

    prompt = input(userInput)
    promptSplitter = prompt[:]
    varDict[promptVar[0]] = prompt


    for everything in varDict.values():


        if everything in promptSplitter:
            write(everything)



    if '+' or '-' or '/' or '*' in promptSplitter[0]:
        evaluations()


def evaluations():
    global n
    for signs in expression:
        if signs in prompt:
            n = eval(prompt)
            print(prompt, '=', n)


def stringCut(stringOfInterest, whatToCut):
    stringOfInterest.split(whatToCut)


def uIOut():
    global finalPrompt
    global promptVar
    global uiAnswer

    promptSeq = words.split('UI')
    promptJOin = ''.join(promptSeq)
    fPrompt = promptJOin.split('(')
    lPrompt = ''.join(fPrompt)
    fPromptW = lPrompt.split(')')
    finalPrompt = ''.join(fPromptW)
    promptVar = finalPrompt.split('$=')
    finPromptVar = ''.join(promptVar)
    dividerPrompt = finPromptVar.split('^')
    last = dividerPrompt[-1]

    ui(last)



loop = True

while loop:
    with open('scroll.glif', 'r') as readFile:
        for words in readFile:
            inPut.append(words)



            if '//' in words:
                comment()

            if 'XX' in words:
                stringCut(words, words)

            if 'VAR' in words:
                varSetter()

            if '!' in words:
                boolStat()


            if 'WRITE' in words:
                if '!' not in words:
                    writing()

            if 'UI' in words:
                uIOut()

            if words.isdigit():
                intSet()

            if 'RAND' in words:
                RANDOM()
