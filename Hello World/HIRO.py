from simpleLibrary import *

functionLibrary = {}
tokens = ['!', 'WRITE', '+', 'IF', '<', '>', 'in']
expression = ['+', '-', '/', '*']
inPut = []
varDict = {}
isString = False
isInt = False
numList = []
stringList = []
n = {}
bools = []


def varSetter():
    global w

    for chars in tokens:
        w = words.split('VAR')
        wFuncs = words.split('WRITE')
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

    if 'WRITE' in notVars:
        del varDict[notVars]


def in_key_word():
    IN = False
    initIn = words.split('IN')
    inJoin = ''.join(initIn)
    sndIn = inJoin.split('(')
    thirdIn = ''.join(sndIn)
    fourthIn = thirdIn.split(')')
    finalIn = ''.join(fourthIn)
    if 'in' in finalIn:
        IN = True
        # write('true')


def intSet():
    global opNow
    global finalOp
    global summ
    # intense editing underway. Adding math expressions such as multiplication, addition, etc.
    # starting with addition for simplicity.
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


def stringSet():
    isString = True
    isInt = False


def comment():
    if not '//' in words:
        pass

    pass


def boolStat():
    # commands for conditional operators
    global lBool
    global finalCond
    global finalExecution

    cond = words.split('!IF(')
    condJoiner = ''.join(cond)
    condJoinerN = condJoiner.split(')!')
    finalCond = ''.join(condJoinerN)

    bools = []

    for chars in finalCond:
        # put chars for digits as its own list and check the length
        # of the character.
        if chars.isdigit() or chars in tokens[:]:

            bools.append(chars)
            if '\n' in bools:
                bools = []
                print(bools)


    boolDecide = ''.join(bools)
    bareBoolDecide = boolDecide.split('<')
    boolJoin = ''.join(bareBoolDecide)
    bBoolDecideFin = boolJoin.split('>')
    boolFinDecider = ''.join(bBoolDecideFin)
    if boolFinDecider.isdigit():
        numFinal = boolDecide
        lBool = eval(numFinal)
        boolExec()


    elif '-INSIDE-' in finalCond:
            bools.append(chars)
            if '\n' in bools:
                bools = []

            lBoolSplitter = finalCond.split(' ')
            lBoolcond_one = lBoolSplitter[1]
            lBoolcond_two = lBoolSplitter[3]

            if lBoolcond_one in lBoolcond_two:
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


def ui(userInput):
    global prompt
    global promptVal

    prompt = input(userInput)

    varDict[finalPrompt[1]] = prompt
    write(prompt)
    if '+' or '-' or '/' or '*' in prompt:
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
    promptSeq = words.split('UI')
    promptJOin = ''.join(promptSeq)
    fPrompt = promptJOin.split('(')
    lPrompt = ''.join(fPrompt)
    fPromptW = lPrompt.split(')')
    finalPrompt = ''.join(fPromptW)
    ui(finalPrompt)


loop = True

while loop:
    with open('scroll.glif', 'r') as readFile:
        for words in readFile:
            inPut.append(words)

            if '<BRK>' in words:
                loop = False

            if '//' in words:
                comment()

            if 'XX' in words:
                stringCut(words, words)

            if '!' in words:
                boolStat()

            if 'VAR' in words:
                varSetter()

            if 'WRITE' in words:
                if '!' not in words:
                    writing()

            if 'UI' in words:
                uIOut()

            if words.isdigit():
                intSet()

