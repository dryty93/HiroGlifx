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
        keywords = ['loop_through', 'write', '$', '$^', '#', '@inside@', 'data_store', '&BluePrint&',
                    'rand5', 'rand50', 'rand100', 'dict', 'def func', '!if', 'brk', 'UI', 'list']

        function_AST = [items for count,items in enumerate(function_contents) if keywords[count]
                        in items]
        print(function_AST)
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
        readFile = StartInterpret.readFile
        line = StartInterpret.line
        expression_line = []

        if '\n' or '/*' in line:
            line = next(readFile)

        if '}' not in line:
            line = next(readFile)
            expression_line.append(line.split("\n")[0].split("  ")[-1])


            if "    " in line:
                function_do = [operators for operators in line.split("  ")[-1].split("\n")[0]]
                line = next(readFile)
                if '}' in line:
                    line = next(readFile)

                if 'func' not in line and '\n' in line or '/*' in line:
                    line = next(readFile)
            get_parameter_initial_values = (line.split("(")[-1].split("\n")[0].split(")")[0])
        get_parameter_initial_values = [ parameters for parameters in get_parameter_initial_values.split(",")  if ',' not in parameters
                                         ]


        replace = [i for i in parameter_find if i.isalpha()]
        print(expression_line,'el')
        for i in range(len(get_parameter_initial_values)):
            function_dictionary[function_name] = {}
            for i in range(len(replace)):
                if len(get_parameter_initial_values) > i:
                    function_dictionary[function_name][replace[i]] = get_parameter_initial_values[i]
                else:
                    function_dictionary[function_name][replace[i]] = expression_line
        for i in function_do:
            try:
                if i  in function_dictionary[function_name][i]:
                    print(i)
            except:
                    # i need to update final_function when it sees a different logical operator

                    final_function = (str(get_parameter_initial_values).replace(',',i))
                    final_function = final_function.replace("'"," ")
                    return_this = (eval(final_function))
                    return_this =[answer for answer in return_this]

        try:
            print(return_this[0])
        except:
            print(final_function)










