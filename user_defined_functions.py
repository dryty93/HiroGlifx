function_dictionary = {}

class Functions():
    def __init__(self,*args):
        pass
    def init_function(self, *args):
        """This splits the line into the variable parameters given within the function to parameter_find"""
        from main import StartInterpret
        global parameter_find
        line = StartInterpret.line
        parameter_find = line.split("(")[-1].split("\n")[0].split(')')[0]
        self.set_parameters()

    def set_parameters(self,*args):
        """This function puts parameters into a list to prepare them for mapping"""
        from main import StartInterpret
        global function_name
        global readFile, line

        parameter_list_counter = 0
        line = StartInterpret.line
        readFile = StartInterpret.readFile
        function_name = line.split('func')[-1].split('(')[0].split(' ')[-1] + ' func'

        parameter_len = len(parameter_find)
        parameter_list = [parameter_item for parameter_item in parameter_find if parameter_item is not ',' and
                          parameter_len < 10]
        if parameter_len > 0:


            self.set_parameter_values()
        else:
            self.get_function_contents()

    def get_function_contents(self):
        """This function searches within the curly braces and returns
        the contents of each function"""
        global function_contents
        function_contents = []
        for i in readFile:
            if '}' not in i:
                if '{' not in i:
                    if type(function_contents) is list:
                        function_contents.append(i.split("  ")[-1].split("\n")[0])

            else:
               # function_contents = " ".join(list(function_contents))
                self.get_keywords()
                break

    def get_keywords(self):
        global keywords
        keywords = ['loop_through', 'write', '$', '$^', '#', '@inside@', 'data_store', '&BluePrint&',
                    'rand5', 'rand50', 'rand100', 'dict', 'def func', '!if(', 'brk', 'UI', 'list']


        function_AST = [items for count,items in enumerate(function_contents) if keywords[count]
                        in items]
        #print(function_AST.count("each_keyword"))
        for items in function_AST:
            if 'write' in items:
                func_in_func_name = items.split("(")[-1].split(")")[0]
                function_in_function_dictionary = {items.split("(")[0]: func_in_func_name}
                func_in_func_name = items.split("(")[0]
                print(func_in_func_name)

    def set_parameter_values(self,*args):
        """This finds logical operators and assigns the value of the given parameters to the variable parameters
        defined in parameter_list. It puts the variable names as keys and the values as the given parameters. And then
        it evaluates the expression given and returns the evaluation."""

        global readFile
        from main import StartInterpret
        from variable import Variable
        from variable import var_look_up_list, varDict
        readFile = StartInterpret.readFile
        line = StartInterpret.line
        expression_line = []
        function_body = 0

        if '\n' or '/*' in line:
            line = next(readFile)

        if '}' not in line:
            line = next(readFile)
            expression_line.append(line.split("\n")[0].split("  ")[-1])

              #  print(expressions)
            if "    " in line:
                function_body = True
               # for words in keywords:
                   # if words in line.split(" "):
                  #    print(words)
                function_do = [operators for operators in line.split("  ")[-1].split("\n")[0]]
                line = next(readFile)

                if 'func' not in line and '\n' in line or '/*' in line:
                    line = next(readFile)
            get_parameter_initial_values = (line.split("(")[-1].split("\n")[0].split(")")[0])
        get_parameter_initial_values = [ parameters for parameters in get_parameter_initial_values.split(",")  if ',' not in parameters
                                         ]


        replace = [i for i in parameter_find if i.isalpha()]

        for i in range(len(get_parameter_initial_values)):
            function_dictionary[function_name] = {}
            for i in range(len(replace)):
                if len(get_parameter_initial_values) > i:
                    function_dictionary[function_name][replace[i]] = get_parameter_initial_values[i]
                else:
                   function_dictionary[function_name][replace[i]] = expression_line


       # print(get_parameter_initial_values)

        final_function = function_do
        end = []


        for i in final_function:
            for k in function_dictionary[function_name]:
                if k in i:
                    end.append(function_dictionary[function_name][i])

            if i not in function_dictionary[function_name].keys():
                if '#' or '$' not in i:
                    end.append(i)
                if '#' or '$' in i:
                    Variable().varLookUp(i)

                    #end.append(var_look_up_list[0])

#        print(end)
        for items in end:
            if 'var' in items:
                    var_val_cross_reference = varDict[items]
                   # var_val_cross_reference = varDict[var_val_cross_reference]


                    if '#' or '$' in var_val_cross_reference:
                        if items in end:
                            end = ''.join(end)
                            end = end.replace(items,str(var_val_cross_reference))

        final_function = ''.join(end)

        return_this = (eval(final_function))
        if '=' in line:
            data_storage = line.split("@ds")

            var_name = data_storage[1].split("var")[0].split(" ")[1]
            var_data = return_this
            Variable().func_var_creation(var_name, var_data)







