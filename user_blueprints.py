#get class name
# create dict for class and set function names as
# keys and their contents as values

bp_global_dictionary = {}
bp_names_in_list = []

class UserBP():
    def __init__(self):
        pass

    def bp_find_name(self, bp_name):
        bp_name = bp_name.split("for")[-1].split("&")[0].split(" ")[-1]
        bp_global_dictionary[bp_name] = []
        bp_names_in_list.append(bp_name)


    def bp_get_attributes(self,attribute):
        bp_attributes = attribute.split('(')[-1].split(')')[0]
        bp_global_dictionary[bp_names_in_list[0]] = bp_attributes
        print(bp_global_dictionary)



