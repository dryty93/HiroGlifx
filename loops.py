from lib_funcs import Lib_Funcs


vals_and_data_list = []
items_to_execute_list = []
execute_items_final_list = []
def loopThrough():
    from main import StartInterpret

    line = StartInterpret.line

    iter_amount = line.split("=")[1].split(":")[0]
   # print(iter_amount,'iteramt')
    vals_and_data = line.split("(")[-1].split(")")
    vals_and_data = vals_and_data[0].split(":")
    vals = vals_and_data[0].split("=")
    vals = vals[-1]
    vals_and_data.append(vals)

    data = vals_and_data[-1].split("=")
    data = data[-1]
    if "\n" in line:
        execution = line.split("\n")[1]

        data_for_function = execution.split("(")[-1].split(")")
        data_for_function = data_for_function[0]

        if 'write' in execution:
            if ',' not in execution:
                for i in range(int(iter_amount) - 1):
                    Lib_Funcs().write()
            if ',' in execution:
                execution = execution.split(',')
                for i in execution:
                    if len(items_to_execute_list) < len(execution):
                        items_to_execute_list.append(execution)
                    if len(items_to_execute_list) >= len(execution):
                        items_to_execute_list.pop(-1)

                for x in range(int(iter_amount)):
                    items_to_execute = " ".join(items_to_execute_list[0])
                    items_to_execute = str(items_to_execute).split("write(")
                    items_to_execute = str(items_to_execute).split(")")
                    items_to_execute = str(items_to_execute).replace(" ", "")
                    if len(execute_items_final_list) == len(execution):
                        for finalIteration in range(int(iter_amount)):
                            print(" ".join(execute_items_final_list))

                    for items in items_to_execute:
                        if items.isdigit():
                            execute_items_final_list.append(items)
                        if items.isalpha():
                            execute_items_final_list.append(items)







