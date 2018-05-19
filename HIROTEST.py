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


with open('HIRO.glif','r') as readFile:

    for words in readFile:


        name = words.split('#')
        fVarName = name[1:-1]
        fVarNamesList.append(fVarName)
        varVals = words.split('=')

        if len(varVals)== 2:
            h.append(words)
        if '\n' in words:
            ' '.join(h)

        for word in words.split('VAR'):

            VARS.append(word)

        for chars in VARS:
                indChars.append(chars)


        def getType():
            global addition
            global subtraction
            global varS
            global counter

            for elements in VARS:


                if '#=' in elements[0:]:

                    variables = elements[3:-1]
                    NUMS.append(variables)
                    varVals.append(NUMS)

                    if '=' in elements[0:]:
                        variables = elements[3:-1]
                        NUMS.append(variables)

                        print("#" + variables)


                        if '+' in variables[:]:
                            digOnly = variables.split('+')
                            numbers = digOnly[:-1]
                            add = (eval(variables))
                            addition.append(add)
                            print(add)

                        if '+' not in variables[:]:
                            addition = []


                        if '-' in variables[:]:
                            digOnly = variables.split('-')
                            numbers = digOnly[:-1]
                            subtract = (eval(variables))
                            subtraction.append(subtract)
                            print(subtract)



                        else:
                            subtraction = []

