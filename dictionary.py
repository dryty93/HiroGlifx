dictOfDicts = {}
dictIter = 0
listOfDicts = []
keys = []
vals = []
countNow = 0
num = 0
dictNumHandler = []
pyToHiDictConv = []
hiroDictIndex = 0
eachDict = []


class Dictionary():

    def dictMaker(self):
        from main import StartInterpret
        global aNum
        global num
        global counter
        global countNow
        global dictIter
        global lenOfDictsList
        global py_to_hiro_pass_line_var
        global num_of_dicts_in_hiro_dic_list

        line = StartInterpret.line
        num_of_dicts_in_hiro_dic_list = 0
        dictIter += 1
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

        state = 0
        dictInfo = py_to_hiro_pass_line_var.split("dict")[-1].split("=")
        dictWrittenName = dictInfo[0].split(" ")[1]
        dictKeysAndVals = dictInfo[-1].split("\n")[0]

        #hiroDictIndex = len(pyToHiDictConv)
        for i in range(lenOfDictsList):
            if len(eachDict) < len(dictOfDicts):
                eachDict.append("dict"+" " + dictWrittenName +" " + "=" + dictKeysAndVals)



    def init_indexDict(self):
        """This functions creates an index for the dictionary
        in proper HiroGlifx syntax"""


        from main import StartInterpret
        line = StartInterpret.line

        count_times_init_runs = 0
        num_of_dicts_in_hiro_dic_list_indexed_for_python = count_times_init_runs - 1
        dict_list_hold = []
        nameDictList = []
        hiro_dic_index_val = line.split(":")[-1].split(")")[0]
        hiro_dic_index_val = int(hiro_dic_index_val) - 1
        user_requested_dict_name =  line.split(":")[0].split("(")[-1]
        final_list_conversion = []

        for i in eachDict:

            nameDict = i.split("=")[0]
            nameDictList.append(nameDict)
            dictDataList = i.split("=")[-1].split(",")
            dict_list_hold.append(dictDataList)

        print(user_requested_dict_name,'index',hiro_dic_index_val + 1,':',dictDataList[hiro_dic_index_val])

        if num_of_dicts_in_hiro_dic_list > 0:
          #  print(count_times_init_runs,'count')
            pass
            if count_times_init_runs < 1:
            #    print(nameDictList,dict_list_hold[num_of_dicts_in_hiro_dic_list_indexed_for_python])
                count_times_init_runs += 1

        if num_of_dicts_in_hiro_dic_list < 1:
            pass
            #print(nameDictList,dict_list_hold[0])
        #global state
        #print('in')
        #state = 1
        #if state == 0:
         #   state += 1
        #    self.pyToHiDict()


        hiroDictIndex = len(pyToHiDictConv)
        #for amount in range(len(dict_list_hold)):
        hiro_test_key = str(dict_list_hold[0][:]).split(">")[0].split("'")[-1].split(" ")[-1]

        #print(hiro_test_key)
        for keys in range(len(dict_list_hold[0])):
            pass
           # print(keys,len(dict_list_hold))
           # if len(dict_list_hold[0]) > 0:
           #         keycount = keys - 1
            #        print(keys,dict_list_hold[keys])
            #if len(dict_list_hold[0]) == 0:
             #   keys = len(dict_list_hold)
              #  print(keys,dict_list_hold[keys])


if __name__=='__main__':
    print("Dictionary Class:"
          "\nThis module is used to create and handle dictionaries."
          "\nIf dictionaries need to be evaluated with boolean logic "
          "\nor with functions (i.e. write function) then"
          "\nthey need to be indexed and saved as variables." )




