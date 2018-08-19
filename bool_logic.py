from lib_funcs import Lib_Funcs

if_not_list = []
if_list = []
class Bools():

    def __init__(self):
        self.line = None
        self.readFile = None

    def ifs_init(self):
        from main import StartInterpret

        line = StartInterpret.line
        readFile = StartInterpret.readFile

        condition_to_validate = line.split('!')[1].split("(")
        code_to_execute = line.split("{")
        if "\n" in code_to_execute:
            code_to_execute = next(readFile)
            code_to_execute = code_to_execute.split("}")[0]


                #if " " in writeMe[0]:
                  #  print(writeMe[0],'blankspace')

     #   print(code_to_execute,'check for execute')
        countLines = 0

        if_or_if_not = condition_to_validate[0]
        condition_to_validate = condition_to_validate[-1].split(")")[0]
        if 'var' not in condition_to_validate:
            truth_detection = eval(condition_to_validate)
            if truth_detection:
                if 'write' in code_to_execute and "$" or "!" not in code_to_execute:
                    try:
                        write_me = code_to_execute.split("(")[1].split(")")[0]
                        if 'var' not in write_me:
                            print(write_me)

                    except:
                        exit('HiroGlifx Interpretter: Syntax Error. write function not written correctly.')




        if '@inside@' not in condition_to_validate[1]:
           # print(condition_to_validate)
            pass

        if 'if' in if_or_if_not:
            if_list.append(if_or_if_not)
        if 'IF-NOT' in if_or_if_not:
            if_not_list.append(if_or_if_not)
