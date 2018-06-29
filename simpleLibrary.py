"""
Author: Tyler J Dryden
Tile:Simple Library
Python 3.6
2018
"""



def types(varType):

    # changes string type
    if isinstance(varType, int):

        n = str(varType)
        print(n)
    if isinstance(varType, str):

        n = str(varType)

def ListConcat(iterVal,oldList, newList, wordToAdd ):

    if not isinstance(iterVal, int):
        write('not str')
        changeVal = str(iterVal)
    for iterVal in oldList:
        newList.append(wordToAdd)
        write(newList)


def write(textToScreen):
    write = print(textToScreen)


def ListToString(List):
    join = ' '.join(List)
    print(join)



