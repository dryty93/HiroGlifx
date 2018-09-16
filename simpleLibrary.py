"""
Author: Tyler J Dryden
Tile:Simple Library
Python 3.6
2018
"""
keywords = ['loop_through', 'write', '$','$^','#','@inside@','data_store','&BluePrint&',
            'rand5','rand50','rand100','dict','def func', '!if','brk','UI','list']
for words in keywords:
    if 'loop_through' in words:
        print(words)

def get_value_for_function_to_execute(function):
    """This splits functions and their value"""
    function_execute = function.split("(")
    function_name = function_execute[0]
    function_execute = function_execute[-1].split(")")[0]
   # return function_name

get_value_for_function_to_execute('write(hello)')

def replace_value_with_definition(current_dict,key_to_find, definition):
    for key in current_dict.keys():
        if key == key_to_find:
            current_dict[key] = definition

    #replace_value_with_definition(replacement="%s")

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


def write(textToScreen,*args):
    write = print(textToScreen,*args)

write('hi','i','you')

def ListToString(List):
    join = ' '.join(List)
    print(join)



