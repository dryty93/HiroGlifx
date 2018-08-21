function_dictionary = {}

class Functions():
    def __init__(self,*args):
        pass
    def init_function(self, *args):
        """This splits the line into respective keywords for mapping"""
        from main import StartInterpret
        global parameter_find
        line = StartInterpret.line
        parameter_find = line.split("(")[-1].split("\n")[0].split(')')[0]

        self.set_parameters()

    def set_parameters(self,*args):
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
        global readFile
        from main import StartInterpret
        readFile = StartInterpret.readFile
        line = StartInterpret.line
        expression_line = []

        if '}' not in line:
            line = next(readFile)
            expression_line.append(line.split("\n")[0].split("  ")[-1])


            if "    " in line:
                line = next(readFile)
                if '}' in line:
                    line = next(readFile)

        get_parameter_initial_values = [ parameters for parameters in line.split("(")[-1].split("\n")[0]  if ',' not in parameters and
                                         ')' not in parameters ]
        #get_parameter_initial_values.append(parameter_find)
        l = len(get_parameter_initial_values)
        l += 2
        replace = [i for i in parameter_find if i.isalpha()]

        for i in range(len(get_parameter_initial_values)):
            function_dictionary[function_name] = {}
            for i in range(len(replace)):
                function_dictionary[function_name][get_parameter_initial_values[i]] = replace[i]
                print(function_dictionary)
          #  function_dictionary[function_name][get_parameter_initial_values[0:i+1]] = {}

        get_parameter_final_values = [params for params in str(expression_line).split(']') if params.isdigit()]
        print(str(get_parameter_final_values),'we')
        for i in range(len(get_parameter_final_values)):
            print(get_parameter_final_values[i])
      # expression_line = str(expression_line).replace()

       # replace = (" ").join(replace)[0]
        print(replace)
        print(function_dictionary)









