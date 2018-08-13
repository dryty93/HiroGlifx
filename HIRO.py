from simpleLibrary import *
from random import randrange


listOfLists = []
exList = []
anotherList = []
functionLibrary = {}
tokens = ['!', 'write', '+', '!if', '<', '>', '@inside@', 'var','!IF-NOT', 'UI','DEF','brk']
expression = ['+', '-', '/', '*']
inPut = []
varDict = {}
listDict = {}
dictOfDicts = {}
functDict = {}
isString = False
isInt = False
numList = []
stringList = []
n = {}
trueList = []
bools = []
randomList = []
newList = []
paramList = []


def boolSep(string):
    """This seperates booleans based on < or >"""
    stringSplitL = string.split('<')
    stringSplitR = string.split('>')
    stringSplitLJoint = stringSplitL[0]
    stringSplitRJoint = stringSplitR[0]


def varSetter():
    global w
    global insideFunction
    global chars


    for chars in tokens:
        w = words.split('var')
        wFuncs = words.split('write')
        insideFunction = words.split('@INSIDE@')
        uIFuncs = words.split('UI')
        n = ' '.join(w)
        rawValFunct = n.split('(')

        if chars not in w:

            if '#' or '$' in chars:
                vVal = str(w[-1])

                varDict[str(w[0])] = str(w[-1])


    for elements in varDict:
        intOccurs = elements.count('#')

        if '#' in elements:
            numList.append(elements)
            intSet()

        if '$' in elements:
            stringList.append(elements)
            stringSet()

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

    if '-'  in words and '!' not in words:
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
    global words
    isString = True
    isInt = False
    if "''" in words:
        words = words.split("''")
        print(words,'string')


def comment():
    if  '/*' in words:
        commentS = words.split('/*')
        commentS =str(commentS[1].split('/'))
        commentS = commentS[0]
        commentS = False

def randFive():
    global rightRand
    global randomVarF

    randomVar = str(randrange(1, 6))
    randomList.append(randomVar)
    randomVarF = str(randomList[0])
    leftRand = str(w[0])
    rightRand = str(w[-1])

    #if '=' not in rightRand:
    varDict[str(w[0])] = randomVarF


def randTen():
    randomVar = str(randrange(1, 11))
    randomList.append(randomVar)
    randomVarF = str(randomList[0])
    varDict[str(w[0])] = randomVarF

def randHun():
    randomVar = str(randrange(1, 101))
    randomList.append(randomVar)
    randomVarF = str(randomList[0])
    varDict[str(w[0])] = randomVarF

def RANDOM():
    '''Creates random ranges in increments of 1-5, 1-10 and 1-100'''
    global randomList
    global randomVarF


    if 'RAND5' in words:
        randFive()

    if 'RAND100' in words:
        randHun()

    if 'RAND10' in words:
        randTen()




def boolStat():
    '''Checks for if conditions and if not conditions
    and passes the data collected to bool Execution.'''


    global lBool
    global nons
    global finalCond
    global finalExecution
    global finalnonCond
    global lBoolSplitLJoint
    global lBoolSplitRJoint

    bools = []
    nons = []
    # created fclist to hold final condition
    fcList= []

    cond = words.split('!if(')
    condJoiner = ''.join(cond)
    condJoinerN = condJoiner.split(')!')
    finalCond = condJoinerN[0]

    if 'if' in words and 'NOT' not in words:
        #print(finalCond,'fcc')
        fcList.append(finalCond)
        if len(fcList) >= 1:
            #finalCond = str(fcList).split(" ")
            #finalCond = str(finalCond).join(",")
           # print(finalCond,'fin')
            condPrep()


    if 'IF-NOT' in words:

        noncond = words.split('!IF-NOT(')
        noncondJoin = ''.join(noncond)
        finalnonSplit = noncondJoin.split(')!')
        finalnonCond = finalnonSplit[0]
       # bools.append(finalnonCond)
        nons.append(finalnonCond)
        condPrep()


def condPrep():
    global bools
    global finalnonCond
    global finalCond
    #print(finalCond)
    if 'var' in finalCond:
       lBoolSplitL = finalCond.split('<')
       lBoolSplitR = finalCond.split('>')
       lBoolSplitEq = finalCond.split('==')
       lBoolSplitUEQ = finalCond.split('!=')
       lBoolSplitLJoint = lBoolSplitL[0]
       lBoolSplitRJoint = lBoolSplitR[0]
       lBoolSplitEqJoint = lBoolSplitEq[0]
       lBoolSplitUEQ = lBoolSplitEq[0]
       lEqR = lBoolSplitEqJoint[:]
       lEqL = lBoolSplitEqJoint[1]

       for everything in varDict:

               if everything in lBoolSplitLJoint and 'NOT' not in lBoolSplitRJoint:

                   convertedKey = str(varDict[everything])
                   finalConvertedKey = convertedKey.split(' ')
                   finalConversionKey = ('').join(finalConvertedKey)
                   finalConvKeyReady = finalConversionKey.split("\n")
                   digAloneKey = ('').join(finalConvKeyReady[0])
                   digAloneFinalkey = digAloneKey.split('=')
                   digKeyF = ('').join(digAloneFinalkey)

                   if '#' in digKeyF:
                       lastConvKey = digKeyF.split('#')
                       lastConvKey = lastConvKey[1]
                       bools.append(lastConvKey)

                   if '$' in digKeyF:
                       lastConvKey = digKeyF.split('$')
                       lastConvKey = lastConvKey[1]
                       bools.append(lastConvKey)

                   if '$^' in digKeyF:
                       lastConvKey = digKeyF.split('$^')
                       lastConvKey = lastConvKey[1]
                       bools.append(lastConvKey)

                   elif digKeyF.isdigit():

                       bools.append(digKeyF)



               if everything in lBoolSplitRJoint and 'NOT' not in lBoolSplitRJoint:

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

               if everything in lBoolSplitEqJoint and 'NOT' not in lBoolSplitEqJoint:

                   convertedKey = str(varDict[everything])

                   finalConvertedKey = convertedKey.split(' ')
                   finalConversionKey = ('').join(finalConvertedKey)
                   finalConvKeyReady = finalConversionKey.split("\n")
                   digAloneKey = ('').join(finalConvKeyReady[0])
                   digAloneFinalkey = digAloneKey.split('=')
                   digKeyF = ('').join(digAloneFinalkey)
                   bools.append(digKeyF)

                   if '#' in digKeyF:
                       lastConvKey = digKeyF.split('#')
                       digitKey = lastConvKey[1]
                       bools.append(digitKey)

                   elif digKeyF.isdigit():
                       bools.append(digKeyF)

               if everything in lBoolSplitUEQ and 'NOT' not in lBoolSplitRJoint:

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
    #nonsnum checks for negation in bools
    nonsNum = len(nons)
    nonList = []
    if nonsNum <= 0:
        if 'var' not in finalCond:
            numFinal = finalCond
            if numFinal[-1] in tokens or numFinal[-1] == ' ':
                pass

            else:
                lBool = eval(numFinal)
                if lBool:
                    boolExec()

        elif 'var' in finalCond:
            finalL = finalCond.split('>')
            char = finalCond.split(' ')
            char = char[5]
            finalL = finalL[0]
            finalR = finalL[-1]
            finalR = finalCond.split('<')
            finalRE = finalR[0]
            finalLE = finalR[-1]
            finalEq = finalCond.split('==')
            finalEqL = finalEq[0]
            finalEqR = finalEq[-1]

            for everything in varDict:


                if finalL or finalR in everything:


                    if varDict[everything].isdigit():
                        n = varDict[everything]


                        trueList.append(n)



             #   print(trueList[:],'lk')

            #print(trueList,'noe')
            if '@inside@' not in char:
                anotherList.append(char)

            if len(anotherList) > 1:
                anotherList.pop(0)

                if trueList[-2].isdigit():
                    tl = str(trueList[-2]) + str("".join(anotherList)) + str(trueList[-1])
                    numFinal = tl

                    lBool = eval(numFinal)
                    if lBool:
                        boolExec()

                  #  if not trueList[-2].isdigit():
                   #     raise Exception("HIRO##:Integer Expected in",'[',str(trueList[-2]),']')
                    #if not trueList[-1].isdigit():
                       # raise Exception("HIRO##:Integer Expected in",'[',str(trueList[-1]),']')

            else:
                if len(trueList) > 1:
                    tl = str(trueList[-2]) + str("".join(anotherList)) + str(trueList[-1])
                    if '>' in tl or '<' in tl or '==' in tl or '!=' in tl:
                        numFinal = tl
                        lBool = eval(numFinal)
                        if lBool:
                            boolExec()

            #if len(trueList) == 2:
                #print(anotherList,'re',trueList)
            #else:
             #   pass
                # if boolFinDecider.isdigit():
                    #    numFinal = boolDecide
                        #print(numFinal,'nf')
                        # this is supposed to check if the last char is a parenthesis
                     #   if numFinal[-1] in tokens or numFinal[-1] == ' ':
                            #print(numFinal)

                      #      pass

    if nonsNum > 0:

        if 'var' not in finalnonCond:
            numFinal = finalnonCond
            if numFinal[-1] in tokens or numFinal[-1] == ' ':
                pass

            else:
                lBool = eval(numFinal)
                if not lBool:
                    boolExec()

        elif 'var' in finalnonCond:

            finalnL = finalnonCond.split('>')
            char = finalnonCond.split(' ')
            char = char[5]
            finalnonL = finalnL[0]
            finalnonR = finalnL[-1]
            finalnR = finalnonCond.split('<')
            finalnonRE = finalnR[0]
            finalnonLE = finalnR[-1]
            finalnEq = finalnonCond.split('==')
            fnjoin = ''.join(finalnL)
            for everything in varDict:


                if everything in finalnonL or everything in finalnonR:

                    if varDict[everything].isdigit():
                        nonList.append(varDict[everything])
                        nonList.append(char)



                    if len(nonList) > 3:
                        nonList.pop(-1)
                        finalnonCond = nonList[0] + nonList[1] + nonList[2]
                        numFinal = finalnonCond

                        lBool = eval(numFinal)
                        if not lBool:
                            boolExec()


                    if boolFinDecider.isdigit():
                        numFinal = boolDecide
                        #print(numFinal,'nf')
                        # this is supposed to check if the last char is a parenthesis
                        if numFinal[-1] in tokens or numFinal[-1] == ' ':
                            #print(numFinal)

                            pass


                    elif '@inside@' in finalnonCond:
                        bools.append(chars)
                        if '\n' in bools:
                            bools = []
                            if 'var' not in finalCond:
                                lBoolSplitter = finalCond.split(' ')
                                lBoolcond_one = lBoolSplitter[1]
                                lBoolcond_two = lBoolSplitter[3]


                                if lBoolcond_one in lBoolcond_two:

                                    lBool = 2 > 1
                                    if lBool:
                                        boolExec()

                            if 'var' in finalCond:
                                lBoolSplit = finalCond.split(' @inside@')
                                lBoolcond_one = lBoolSplit[0]
                                lBoolcond_two_gen = lBoolSplit[1].split('{')
                                lBoolcond_two = lBoolcond_two_gen[0]

                                # needed so python recognizes var keys
                                for everything in varDict:
                                    everyString = everything.split('var $')

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
    """Checks the bool condition for functions or known keywords and executes them"""
    global valueAssign

    writeFun = 2 > 1
    execute = words.split('!')
    exJoin = execute[2]
    exFinal = exJoin.split('{')
    exFi = ''.join(exFinal)
    exFinale = exFi.split('}')
    if "," in exFinale:
        print(exFinale)
    finalExecution = exFinale[0]

    if 'write' in finalExecution:
        writeSequence = finalExecution.split('write')
        writeStringJoin = ''.join(writeSequence)
        fWriteSequence = writeStringJoin.split('(')
        o = ''.join(fWriteSequence)
        fWrite = o.split(')')
        finalWriter = ''.join(fWrite)
        if ',' in finalWriter:

            splitting = finalWriter.split(",")
            print(splitting[0])
            if 'brk' in finalWriter:
                breakNow()
            #if 'write' in finalWriter:

            else:
                for toks in tokens:
                    #print(toks)
                    if toks in finalWriter:

                        exList.append(toks)
                    if len(exList) > 0:
                        exDecider = exList
                        print(exDecider)

           # if tokens[:] in finalWriter:
            #    breakNow()
        else:
            write(finalWriter)
            for everything in varDict:
                if everything in finalWriter:
                    write(varDict[everything])

    if '@inside@' in finalExecution:
        insideSeq = finalExecution.split('@inside@')
        insideJoin = ''.join(insideSeq)
        fInsideSeq = insideJoin.split('(')
        r = ''.join(fInsideSeq)
        fSeq = r.split(')')
        finalSeq = ''.join(fSeq)
        write(finalSeq)
        for everything in varDict:
            if everything in finalSeq:
                varDict[everything]

    if "=" in finalExecution:
        asignPre = finalExecution.split('=')
        valueAssign = str(asignPre[-1])
        varAssign = str(asignPre[0])
        print(valueAssign,'va')
        if 'RAND5' in valueAssign:
             randFive()


        else:
            varDict[varAssign] = valueAssign



def breakNow():

    exit()


def writing():
    # i likely will rewrite this so that it is more reusable for the entire project
    #  because i find myself repeating this same code with little differences for all functions
    #  within the code.
    global eFinale
    global writeSequence

    writeSequence = words.split('write')
    writeStringJoin = ''.join(writeSequence)
    fWriteSequence = writeStringJoin.split('(')
    o = ''.join(fWriteSequence)
    fWrite = o.split(')')


    finalWriter = ''.join(fWrite)

    for everything in varDict.keys():
        if everything in finalWriter and '^' not in finalWriter:


            print(varDict[everything])
    if '^' in finalWriter:
        print(prompt)

def ui(userInput):
    global prompt
    global promptVal
    global promptVar
    global prompted
    prompt = input(userInput)
    promptSplitter = prompt[:]
    prompted = promptVar[0]
    varDict[prompted] = prompt





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

def createFunct(funcName, funcProp):

    if funcParams:
        if 'var' in paramVals:
            for everything in varDict:
                if everything in paramVals[0]:
                    print(everything)

                if everything in paramVals[1]:
                    print(everything)

            funcParamsR = paramVals[0]
            funcParamsL = paramVals[1]
           # print(funcParamsL,funcParamsR)

    if 'WRITE' in funcProp:
        writeNow = funcProp
        writeSplit = writeNow.split('(')
        writeSplitter = writeSplit[1].split(')')
        writeFunEx = ''.join(writeSplitter)
        print(writeFunEx)


def iterHold():
    global loopNum
    global w

    ln = str(loopNum)

    w = ('').join(w[0])

   # w = w.split('(')
    varDict[w] = ln

def listMaker():
    global words
    for i in tokens:


        if i not in words:
            if 'var' not in words:
                potListGen = words.split("\n")
                listGen = str(potListGen).split("list")
                listGen = listGen[1]
                listName = listGen[0]
                listName = str(listName).split("'")
                listGen = str(listGen).split("=")
                listName = listGen[0]
                listVals = str(listGen[1:])
                listDict[listName] = listVals
            else:
                for everything in varDict:
                    if words in everything:
                        print(varDict[everything])




loop = True
loopNum = 0
while loop:
    loopNum += 1
    with open('scroll.glif', 'r') as readFile:
        for words in readFile:


            if "brk" in words:
                loop = 0
                exit()


            if '/*' in words:
                comment()


            if 'XX' in words:
                stringCut(words, words)




            if 'var' in words:
                varSetter()



            if 'LN' in words:
                iterHold()

            if '!' in words:
                if '\n' in words:
                    # words = words.replace("\n", "")

                    words = (words + next(readFile))
                    words = words.split("\n")[:]
                    words = words[0] + words[1]
                    boolStat()



            if 'write' in words:
                if '!' not in words:
                    writing()

            if 'UI' in words:
                uIOut()

            if words.isdigit():
                intSet()

            if 'RAND' in words:
                RANDOM()

            if 'Def' in words:
                funcSplit = words.split('{')
                funcParamsL = words.split('(')
                funcParamsR = words.split(')')
                funcParams = funcParamsL + funcParamsR
                paramVals = ''.join(funcParams)
                paramVals = funcParams[1].split(')')[0].split(',')
                for length in paramVals:
                    if length:
                        paramList.append(length)
                        varDict[length] = length
                        for key in varDict:
                            if length in key:
                                print(length,'le')

                paramList = []
                newList.append(funcParams[:])
                funcParamOne = funcParams[0]

                funcExec = funcSplit[1].split('}')
                functName = words.split(' ')[1].split('(')
                functName = functName[0]
                createFunct(functName, funcExec[0])

            if 'list' in words:
                listMaker()
