
# this function was taken from a previous branch of HiroGlifx. I am refactoring it to work
# in accordance with the rest of the modules within this directory.
def listMaker():
    from main import StartInterpret

    line = StartInterpret.line
    listDic = {}

    vNum = 0
    tokens = ['!', 'write', '+', '!if', '<', '>', '@inside@', 'var', '!IF-NOT', 'UI', 'DEF', 'brk', 'list', 'dic']

    for i in tokens:
        if i not in line:

            if 'write' not in line:
                potListGen = line.split("\n")
                listGen = str(potListGen).split("list")
                listGen = listGen[1]
                listName = listGen[0]
                listName = str(listName).split("'")
                listGen = str(listGen).split("=")
                listName = listGen[0]
                listVals = str(listGen[1])
                varListValue = listVals.split(",")

                if '$' in listVals:
                    varValGet = listVals.split('$')
                    varValGet = varValGet[0]


                if '#' in listVals:
                    varValGet = listVals.split('#')
                    varValGet = varValGet[0]
                    listVarCounter = listVals.split('var')
                    print(listVarCounter)
                    for i in listVarCounter:
                        if 'var' in i:
                            vNum += 1
                            print(vNum,'vNum')
                if 'var' not in listVals:
                    listDict[listName] = listVals
                  #  print(listDict)

                if 'var' in line:

                    for elements in listVals.split(","):
                        for everything in varDict:
                            # this expression makes sure that the element is not a variable or a list and pops
                            # the last character of the string so that it matches the key in
                            # the variable dictionary (varDict)
                            if 'var' in elements:
                                if 'list' not in elements:
                                    if 'dict' not in elements:
                                        vKey = elements.split(" ")
                                        vKey.pop(-1)
                                        vKey = vKey[1] + " " + vKey[2]

                                        if vKey in everything:
                                            varHold = varDict[everything]
                                            if len(varHold) > 4:
                                                pp = varHold
                                                pnum = len(pp) * 2
                                                exList.append(pp)
                                                listVals = varValGet + varHold
                                                listDict[listName] = listVals
                                        if len(listOfLists) > len(listVals):
                                            listOfLists.pop(0)
                                leee = len(listDict)
                                if leee == 1:
                                    if len(listOfLists) < 4:
                                        listOfLists.append(listVals)
                                        listOfLists.append(pp)
                                        leee += 1
                                else:
                                    nun = 4

                                    pass
            if 'write' in words:
                if ',' not in words:
                    listName = words.split("list")[-1].split(")")[0] + " "

                    listPrinted = listName + ":" + listDict[listName]
    try:
        print(listPrinted)
    except:
        pass