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

        parameter_list_counter = 0
        line = StartInterpret.line
        readFile = StartInterpret.readFile
        function_name = line.split('func')[-1].split('(')[0].split(' ')[-1] + ' func'

        parameter_len = len(parameter_find)
        parameter_list = [parameter_item for parameter_item in parameter_find if parameter_item is not ',' and
                          parameter_len < 10]

        self.set_parameter_values()

    def set_parameter_values(self,*args):
        """This finds logical operators and assigns the value of the given parameters to the variable parameters
        defined in parameter_list. It puts the variable names as keys and the values as the given parameters. And then
        it evaluates the expression given and returns the evaluation."""
        global readFile
        from main import StartInterpret
        readFile = StartInterpret.readFile
        line = StartInterpret.line
        expression_line = []

        if '\n' in line:
            line = next(readFile)

        if '}' not in line:
            line = next(readFile)
            expression_line.append(line.split("\n")[0].split("  ")[-1])


            if "    " in line:
                function_do = [operators for operators in line.split("  ")[-1].split("\n")[0]]
#                print(function_do)
                line = next(readFile)
                if '}' in line:
                    line = next(readFile)

            get_parameter_initial_values = (line.split("(")[-1].split("\n")[0].split(")")[0])
        get_parameter_initial_values = [ parameters for parameters in get_parameter_initial_values.split(",")  if ',' not in parameters
                                         ]
        replace = [i for i in parameter_find if i.isalpha()]

        for i in range(len(get_parameter_initial_values)):
            function_dictionary[function_name] = {}
            for i in range(len(replace)):
                function_dictionary[function_name][replace[i]] = get_parameter_initial_values[i]

        get_parameter_final_values = [params for params in str(expression_line).split(']') if params.isdigit()]

        n = 0
        for i in function_do:
            try:
                if i  in function_dictionary[function_name][i]:
                    print(i)
            except:
                   # print(i)
                    # i need to update final_function when it sees a different logical operator
                    if not i.isdigit():
                       print(i)
                    final_function = (str(get_parameter_initial_values).replace(',',i))
                    final_function = final_function.replace("'"," ")
                    n += 1
                    return_this = (eval(final_function))

                    return_this =[answer for answer in return_this]

        try:
            print(return_this[0])
        except:
            pass










