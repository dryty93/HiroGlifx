dictOfDicts = {}
listOfDicts = []
keys = []
vals = []
countNow = 0
num = 0
dictNumHandler = []
pyToHiDictConv = []
hiroDictIndex = 0
eachDict = []
dict_of_hi_dicts = {}
dict_of_hi_dicts_final_conversion = {}
hiro_dicts_name_list = []
hiro_key_val_map = {}


class Dictionary():

    def dictMaker(self):
        from main import StartInterpret
        global num
        global countNow
        global lenOfDictsList
        global py_to_hiro_pass_line_var
        global num_of_dicts_in_hiro_dic_list

        line = StartInterpret.line
        num_of_dicts_in_hiro_dic_list = 0
        dictName = line.rstrip("\n")
        dictName = dictName.split(" ")
        dictVals = dictName[3:]
        dictName = dictName[1]
        dictOfDicts[dictName] = {}
        synListConv = []
        dictListName = []

        for count in dictVals:
            fVals = count.split(", ")
            if '>' in count:
                keyValDiv = count.split(">")
                listOfDicts.append(fVals)
                keys.append(keyValDiv[0])
                vals.append(keyValDiv[-1])
                lenOfDictsList = len(listOfDicts)

        if len(listOfDicts) > len(dictVals):
            listOfDicts.pop(0)

        for kv in keys:
            keyFind = len(keys)

            if countNow < keyFind:
                if len(dictOfDicts) < 2:
                    dictOfDicts[dictName][kv] = vals[countNow]
                    countNow += 1
            if len(dictOfDicts) >= 2:
                keyFinder = len(keys)
                valFinder = len(vals)

            # checks how many dictionaries are in dictofdicts and seperates
            # keys and values into their respective sub-dictionaries
            if len(dictOfDicts) >= 1:
                while num < len(keys):
                    if num <= len(keys):
                        dictNumHandler.append(num)
                        dictOfDicts[dictName][keys[num]] = vals[dictNumHandler[num]]
                        num += 1
                    if num > len(keys):
                        pass

        # print(dictOfDicts)
        for i in dictOfDicts.items():
            if 'write' not in line:
                countKeys = str(i).count(":")
                nOfDict = str(i).split(',')
                dictListName.append(nOfDict[0])
                dictVals = str(i[1:]).split("}")[0].split("{")[1]
                lenDVal = len(dictVals)
                dictVals = dictVals.replace(":", '>')
                listOfConvDicts = "dict"
                listOfConvDicts += dictListName[num_of_dicts_in_hiro_dic_list].split("(")[1]
                listOfConvDicts.join(" ")
                listOfConvDicts += '=' + dictVals
                synListConv.append(listOfConvDicts)
                num_of_dicts_in_hiro_dic_list = num_of_dicts_in_hiro_dic_list + 1
                py_to_hiro_pass_line_var = line
                self.pyToHiDict()

    def pyToHiDict(self):
        """ This converts python dictionary syntax to Hiro
        dictionary syntax for the view of the user"""
        global dict_of_hi_dicts_final_conversion
        global dictWrittenName

        state = 0
        dictInfo = py_to_hiro_pass_line_var.split("dict")[-1].split("=")
        dictWrittenName = dictInfo[0].split(" ")[1]
        dictKeysAndVals = dictInfo[-1].split("\n")[0]
        #hiroDictIndex = len(pyToHiDictConv)
        for i in range(lenOfDictsList):
            if len(eachDict) < len(dictOfDicts):
                eachDict.append(dictKeysAndVals)
                hiro_dicts_name_list.append(dictWrittenName)
                dict_of_hi_dicts[dictWrittenName] = eachDict[i]
            if len(eachDict) > 0:
                dicts_indexer = [items for items in eachDict]
                if i < len(dicts_indexer):
                    dict_of_hi_dicts_final_conversion[dictWrittenName] = dicts_indexer[i]


    def init_indexDict(self):
        """This functions creates an index for the dictionary
        in proper HiroGlifx syntax and returns it to the user"""
        from main import StartInterpret
    # introduced new bug. Now user has to reference dictionary if dictionaries are
    # created. Need to fix this immediately.

        line = StartInterpret.line
        dict_look_up = StartInterpret.dict_look_up
        dict_look_up = dict_look_up[0].split('^')[-1].split("\n")[0]
        written_hiro_dictionary_name_by_itself = line.split("dict")[-1].split("\n")[0].split(" ")[-1].split(")")[0]
        print(dict_of_hi_dicts_final_conversion.keys())
        for items in dict_of_hi_dicts_final_conversion.keys():
            if written_hiro_dictionary_name_by_itself in items:
                dictionary_initial_index = 'dict '+ items +' ='+dict_of_hi_dicts_final_conversion[items]
        hi_dicts_key_val_map_preparer = eachDict[0].split(",")
        # this counts keys and appends to the count_hi_dicts_key_val_map_preparer
        count_hi_dicts_key_val_map_preparer_function = lambda count_keys: count_keys + 1 if count_keys < 3 else (
                    count_keys == 0)
        count_hi_dicts_key_val_map_preparer = [key for key in hi_dicts_key_val_map_preparer if
                                               count_hi_dicts_key_val_map_preparer_function]
        print(count_hi_dicts_key_val_map_preparer)
        for i in range(len(count_hi_dicts_key_val_map_preparer)):
            if i <= len(count_hi_dicts_key_val_map_preparer):
                hiro_key_val_map[count_hi_dicts_key_val_map_preparer[i].split(">")[0]] = count_hi_dicts_key_val_map_preparer[i].split(">")[-1]

        # need to implement something so that the interpretter takes the users requested key
        # looks it up against the dictionary and returns the proper dictionary item. Right now
        try:
            print(dict_look_up)
            print(hiro_key_val_map[dict_look_up])
        except:
            exit('HiroGlifx Interpretter: Key-Val Error: \nSpecified Key Not Found!')


if __name__=='__main__':
    print("Dictionary Class:"
          "\nThis module is used to create and handle dictionaries."
          "\nIf dictionaries need to be evaluated with boolean logic "
          "\nor with functions (i.e. write function) then"
          "\nthey need to be indexed and saved as variables." )




