# this function was taken from a previous branch of HiroGlifx. I am refactoring it to work
# in accordance with the rest of the modules within this directory.
def listMaker():
    from main import StartInterpret
    from variable import Variable

    line = StartInterpret.line

    listDict = {}

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
                    print(listDict,listVals)
                print(listDict)

                if 'var' in line:

                    print(line)
            if 'write' in line:
                if ',' not in line:
                    listName = line.split("list")[-1].split(")")[0] + " "

                    listPrinted = listName + ":" + listDict[listName]
                    try:
                        print(listPrinted)
                    except:
                        pass
listMaker()