from lineCount import countLines
from variable import Variable
from dictionary import Dictionary
from lib_funcs import Lib_Funcs
from loops import loopThrough
from bool_logic import Bools
from lineCount import line_location
from user_defined_functions import Functions

import time


countLines()


print("Hir\x07Glifx v.0.1:")

class StartInterpret():

    def __init__(self):
        pass

    def initialize_interpreter(self):
        """This starts the HiroGlifx interpretter """

        time.sleep(1)
        print("Interpretting.\x07.\x07.\x07")
        self.run_interpreter()

    @classmethod
    def run_interpreter(self):
        while True:


            line_list = []
            with open('scroll.glif', 'r') as readFile:

                self.readFile = readFile
                self.line_list = line_list

                for line in readFile:
                    self.line = line


                  #  print(self.line_class_var)
                    #print(self.line)

                    var = Variable()


                    if '/*' in self.line:
                        self.line = next(self.readFile)


                    if 'loop_through' in line:
                        self.line = self.line + next(self.readFile)
                        loopThrough()
                    if '!' in self.line:
                        Bools().ifs_init()
                    if 'dict' in self.line:
                        if 'write' not in self.line:
                            if '!' not in self.line:
                                if 'index' not in line:
                                    Dictionary().dictMaker()
                    if 'var' in self.line:
                        if '!' not in self.line:
                            if 'write' not in self.line:
                                if 'list' not in self.line:
                                    if 'dict' not in self.line:
                                        Variable().newVariable()
                    if 'def func' in self.line:
                        Functions().init_function()
                    if 'write' in line:
                        if 'func' not in line:
                            Lib_Funcs().write()
                    if 'index' in line:
                        Dictionary().init_indexDict()
                    if 'brk' in line:
                      #  print(line_location)

                        exit()



StartInterpret().initialize_interpreter()