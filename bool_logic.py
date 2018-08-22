from lib_funcs import Lib_Funcs

if_not_list = []
if_list = []
class Bools():

    def __init__(self):
        self.line = None
        self.readFile = None

    def ifs_init(self):
        from main import StartInterpret
        from variable import Variable
        from variable import var_look_up_list


        line = StartInterpret.line
        readFile = StartInterpret.readFile


        condition_to_validate = line.split('!')[1].split("(")
        code_to_execute = line.split("{")
        if "\n" in code_to_execute:
            code_to_execute = next(readFile)
            code_to_execute = code_to_execute.split("}")[0]

        if_or_if_not = condition_to_validate[0]
        condition_to_validate = condition_to_validate[-1].split(")")[0]
        if 'var' not in condition_to_validate:
            if '@inside@' not in condition_to_validate:
                truth_detection = eval(condition_to_validate)
                if truth_detection:
                    if 'write' in code_to_execute and "$" or "!" not in code_to_execute:
                        try:
                            write_me = code_to_execute.split("(")[1].split(")")[0]

                            if 'var' not in write_me:
                                print(write_me)
                            if 'var' in write_me:
                                Variable().varLookUp(write_me)
                                print(var_look_up_list[0])
                        except:
                            exit('HiroGlifx Interpretter: Syntax Error. write function not written correctly.')
            if '@inside@' in condition_to_validate:

                self.inside_checker(line)

                if self.inside_checker(line):
                    if 'var' not in line:
                        write_me = code_to_execute.split("(")[1].split(")")[0]
                        print(write_me)

        if 'var' in condition_to_validate:
            # add error handling here because the user needs to leave at least one space
            # between the logical operator and the variable name.

            logical_operator = condition_to_validate.split("#")[2].split(" ")[1]
            if '>' in logical_operator:

                condition_to_validate_left = condition_to_validate.split(">")[0]
                condition_to_validate_right = condition_to_validate.split(">")[-1]

                # print(condition_to_validate_right,'wtf')
                Variable().varLookUp(condition_to_validate_left)
                condition_to_validate_left = var_look_up_list[0]
                Variable().varLookUp(condition_to_validate_right)
                condition_to_validate_right = var_look_up_list[0]
                code_to_execute_var_convert = str(condition_to_validate_left) + logical_operator + str(
                    condition_to_validate_right)
                truth_detection = eval(code_to_execute_var_convert)
                if truth_detection:
                    if 'write' in code_to_execute and "$" or "!" not in code_to_execute:
                        try:
                            write_me = code_to_execute.split("(")[1].split(")")[0]
                            if 'var' not in write_me:
                                print(write_me)
                        except:
                            exit('HiroGlifx Interpretter: Syntax Error. write function not written correctly.')

            if '<' in logical_operator:

                    condition_to_validate_left = line.split("<")[0].split("(")[-1]
                    condition_to_validate_right = line.split("<")[-1].split(")")[0]

                #print(condition_to_validate_right,'wtf')
                    Variable().varLookUp(condition_to_validate_left)
                    condition_to_validate_left = var_look_up_list[0]
                    Variable().varLookUp(condition_to_validate_right)
                    condition_to_validate_right = var_look_up_list[-1]
                    code_to_execute_var_convert = str(condition_to_validate_left) + logical_operator + str(condition_to_validate_right)
                    truth_detection = eval(code_to_execute_var_convert)
                    if truth_detection:
                        if 'write' in code_to_execute and "$" or "!" not in code_to_execute:
                            write_me = code_to_execute.split("(")[1].split(")")[0]
                            if 'var' not in write_me:
                                print(write_me)
                            if 'var' in write_me:
                                Variable().varLookUp(write_me)
                                print(var_look_up_list[-1])
            if '==' in line:
                logical_operator = line.split("#")[1].split("var")[-1]
                condition_to_validate_left = "' "+line.split("==")[0].split("(")[-1] + "# '"
                condition_to_validate_right = line.split("==")[-1].split(")")[0]
                Variable().varLookUp(condition_to_validate_left)
                condition_to_validate_left = var_look_up_list[0]
                Variable().varLookUp(condition_to_validate_right)
                condition_to_validate_right = var_look_up_list[-1]
                code_to_execute_var_convert = str(condition_to_validate_left) + logical_operator + str(condition_to_validate_right)
                truth_detection = eval(code_to_execute_var_convert)
               # if 'not' in line:
                print(line,'line')
                if truth_detection:
                    if 'write' in code_to_execute and "$" or "!" not in code_to_execute:
                        write_me = code_to_execute.split("(")[1].split(")")[0]
                        if 'var' not in write_me:
                            print(write_me)
                        if 'var' in write_me:
                            Variable().varLookUp(write_me)
                            print(var_look_up_list[-1])

        if 'if' in if_or_if_not:
            if_list.append(if_or_if_not)
        if 'IF-NOT' in if_or_if_not:
            if_not_list.append(if_or_if_not)

    def inside_checker(self,validate_this_condition):
        """Checks if one value is in another value """

        validate_this_condition = validate_this_condition.split("@inside@")
        left_side_of_inside_condition = validate_this_condition[0].split("(")[-1]
        right_side_of_inside_condition = validate_this_condition[-1].split(")")[0].split(" ")[-1]
        if right_side_of_inside_condition in left_side_of_inside_condition :
            return True
