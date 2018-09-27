from userInput import uIOut,ui
from random import *
varNameList = []
varValList = []
varCount = 0
varDict = {}
is_num = False
is_str = False
is_user_input = False
list_of_strings = []
list_of_ints = []
var_look_up_list = []
class Variable():
    def __init__(self,):
        pass

    def varDictUpdate(self):
        """This makes variable name a key and variable value a value"""
        from main import StartInterpret
        from lib_funcs import Lib_Funcs

        line = StartInterpret.line
        if 'function' in str(varVal):
            print(varVal)

        if 'rand' in str(varVal):

            random_var_name = line.split("=")[0]
            if 'rand5' in str(varVal):
                random_var_value = str(randrange(1, 6))
            if 'rand10' in str(varVal):
                random_var_value = str(randrange(1, 11))
            if 'rand100' in str(varVal):
                random_var_value = (randrange(1, 101))
            varDict[random_var_name] = random_var_value
        if 'rand' not in str(varVal):
            for items in range(len(varValList)):
                if '/*' not in line:
                    if "$^" not in varName:
                        if 'rand' not in str(varVal):
                            varDict[varName] = varVal


    def newVariable(self):

        from main import StartInterpret
        from lib_funcs import Lib_Funcs

        global write_state_var

        """This splits up the line variable from the main.py file"""
        global varName,varVal,state
        state = 0
        line = StartInterpret.line
        if '/*' not in line:
            varName = line.split('=')[0]

            # var_syntax_char_one/two check vars holds first and last characters of the variables name
            # I then check if these two characters are equal to the appropriate decorator
            # specified in HiroGlifx based on the variable's type

            var_syntax_check_char_one = varName.split("var")
            var_syntax_check_char_two = var_syntax_check_char_one[0].split(" ")[0]
            var_syntax_check_char_one = var_syntax_check_char_one[-1]

            if '$^' in varName:
                uIOut()
            varVal = line.split('=')[-1]
            if '$^' in str(varVal):
                Variable.varLookUp(self,varVal)
                try:
                    varVal = var_look_up_list[-1]
                except:
                    pass
            if '\n' in varVal:
                varVal = varVal.split("\n")[0]
            if "$" in varName and "$^" not in varName:
                is_str = True
                varVal = "'" + varVal + "'"
                varValList.append(varVal)
                # Error Handling
                if '$' not in var_syntax_check_char_one:
                    exit("Hir\7Glifx Interpretter: Syntax Error in variable declaration in "  + "\nString variables should contain the '$' decorator between \nthe variable name and the var keyword \n'Example '$ name var $= Hello ")
                if '$' not in var_syntax_check_char_two:
                    exit("Hir\7Glifx Interpretter: Syntax Error in variable declaration \nString variables should contain the '$' decorator between \n the variable name and the var keyword \n 'Example '$ name var $= Hello ")
            if "#" in varName:
                varValList.append(varVal)
                is_num = True
                if '#' not in var_syntax_check_char_one:
                    exit("Hir\7Glifx Interpretter: Syntax Error Found! \nType: Variable Declaration."  + "\nNum variables should contain the '#' decorator between \nthe variable name and the var keyword. \nExample: # count var #= 4")
                if '#' not in var_syntax_check_char_one:
                    exit("Hir\7Glifx Interpretter: Syntax Error Found! \nType: variable declaration" + "\nNum variables should contain the '$' decorator between \nthe variable name and the var keyword \n'Example '$ name var $= Hello ")

                # Checks if the variable type is num/int and evaluates it if the variable type
                #is a num/int.

                logic_operators = ["+", "*", "**","****" "/", "-"]


                if is_num and 'rand' and 'var' not in varVal:
                    if "+" or "*" or "/" or '**' or "-" or ('***') in varVal:

                        varVal = eval(varVal)
                        list_of_ints.append(varVal)

                if 'var' in str(varVal):
                    for operators in logic_operators:
                        if operators in str(varVal):
                            var_concatenated_expression = str(varVal).split(operators)
                            for i in var_concatenated_expression:
                                if 'var' in i:
                                    Variable.varLookUp(self,i)
                                    new_var = var_look_up_list[-1]
                                    i = new_var
                                    if 'var' not in str(new_var):
                                        try:
                                            new_expression = varVal.replace("var", str(i))
                                            new_expression = new_expression.replace("#"," ")
                                            new_expression = new_expression.split(' ')
                                        except:
                                            pass
                                       # print(new_expression)
                                        for items in new_expression:
                                            if items == '':
                                                if not items.isalpha():
                                                    if not items.isdigit():
                                                        if "+" or "-" or '/' or '*' or '**' or '***' not in items:
                                                            new_expression.remove(items)


                                        new_expression = new_expression[0:-2]
                                        #print(new_expression)

                                        for items in new_expression:
                                            if items.isalpha():
                                                new_expression.remove(items)
                                            if items is None:
                                                new_expression.remove(items)


                                        new_expression = ''.join(new_expression)

                                        try:
                                            varVal = eval(new_expression)
                                        except:
                                            pass


            if 'bool' in varName:
                if (">") or ("<") or ("==") in varVal:
                    try:
                        varVal = eval(varVal)
                    except:
                        exit("Hir\7Glifx Interpretter: Syntax Error Found! \nType:Boolean Evaluation \nPlease only use approved logical operators including '>','<', and '=='.")



            varNameList.append(varName)

            varValList.append(varVal)
            self.varDictUpdate()

    def writeVar(self):
        from main import StartInterpret


        line = line = StartInterpret.line
        if ',' not in line:
            varConvert = line.split("(")[-1].split(")")[0]
            varConvert = varConvert.split('=')[-1]
            for keys in varDict:
                if keys in varConvert:
                    print(varDict[keys])

    def varLookUp(self,var_key_check):

        for keys in varDict:
            if keys in var_key_check:
                var_value = varDict[keys]
                var_look_up_list.append(var_value)
        return var_look_up_list

    def func_var_creation(self,name, value):

        if type(value) == int:
            name = "# " + name +" var " +"#"
        if type(value) == float:
            name = "# " + name + " var " + "#"
        elif type(value) == str:
            name = "$ " + name +" var" +" $"
        varDict[name] = value

if __name__=='__main__':
    print("Variable Class:"
          "\nThis module is used to create and handle variables."
          "\nIf variables need to be evaluated with boolean logic "
          "\nor with functions (i.e. write function) then"
          "\nthe information is passed on to either lib__funcs or"
          "\nbooleanLogic.")
