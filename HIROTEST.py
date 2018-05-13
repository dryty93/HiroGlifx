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
          
          }

keywords = ['WRITE', 'TYPES']


if '!' in tokens:
    #print('ok')
    tokens['!'] = True

# make for loop with counter variable
# and assign dictionary the corresponding values of vars and varvals in scope
#of counter vars

with open('HIRO.glif','r') as readFile:

    for words in readFile:

        if 'WRITE' in words:
            writeSequence = words.split('WRITE')
            writeStringJoin = ''.join(writeSequence)
            fWriteSequence = writeStringJoin.split('(')
            o = ''.join(fWriteSequence)
            fWrite = o.split(')')
            finalWriter = ''.join(fWrite)
            
            write(finalWriter)

        name = words.split('#')
        fVarName = name[1:-1]
        fVarNamesList.append(fVarName)
        varVals = words.split('=')
        #print(varVals)
        if len(varVals)== 2:
            h.append(words)
           # print(h)
        if '\n' in words:
            ' '.join(h)
            #print(h)

        for word in words.split('VAR'):
    
            VARS.append(word)
          #  print(VARS)

        for chars in VARS:
                #print(chars)
                indChars.append(chars)

        #for each time that VARVAL APPEARS get its name and put it in dictionary MEMORY
        MEMORY = dict()
        count = 0

      #  for placeHolder in VARS:
       #     count += 1
            
        #    MEMORY[varNames[count]]= varVals[count]
            
                

        def do():
            if '!' in words:
                tokens['!'] = True

                if tokens:
                    print('conditional')
                else:
                    print('no')


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
                   # print("#" + variables)




                    if '=' in elements[0:]:
                        variables = elements[3:-1]
                        NUMS.append(variables)
                        
                        #print("#" + variables)


                        if '+' in variables[:]:
                            digOnly = variables.split('+')
                            numbers = digOnly[:-1]
                            add = (eval(variables))
                            addition.append(add)
 #                           print(variables, '=',addition)




                        else:
                            addition = []

                        if '-' in variables[:]:
                            digOnly = variables.split('-')
                            numbers = digOnly[:-1]
                            subtract = (eval(variables))
                            subtraction.append(subtract)
#                            print(variables ,'=', subtraction)



                        else:
                            subtraction = []


                if '$=' in elements:

                    variables = elements[3:-1]
                    STRINGS.append(variables)
                    varVals.append(STRINGS)
                   # print(variables)

                    if "'" in variables:
                        varS = variables.split("%s")

                        print(fVarNamesList, '$', varS, '$')

                        #print(variables)

                if '$' or '#' not in elements:
                    varS = []





#print(l)
#print(counter)
readFile.close()
getType()
do()
n = []

c = -1
for i in fVarNamesList:
    c += 1
    #n.append(fVarNamesList[c])
    if c <= len(h):
        if fVarNamesList[c]:
            if '=' not in fVarNamesList[c]:
                n.append(fVarNamesList[c])

dictionary = {}
#dictionary['mynewkey'] = 'mynewvalue'
#print(d)
#dictionary[fVarNamesList[c]] = 

    #n.append(h[i])
    #fVarNamesList.pop(0)
   # print(n)



#for chars in STRINGS:
makeFile = open("hiroglifs.glif", "w+")
makeFile.write(str(n))
makeFile.close()

#print('#', numbers, '#' +  variables)

#print(equations)
