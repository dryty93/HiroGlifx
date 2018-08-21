def progress_scorer():
    items_in_progress = 0
    complete_items = 0
    all_items = 0
    items_left = 0
    syntax = []
    control_flow = []
    data_structures = []
    memory = []
    functions = []
    error_handling = []
    new_line_count = 0
    each_section = []
    bugs = []
    section_list = []


    with open('progress.txt', 'r') as readFile:
        for line in readFile:
            if 'Completion' in line:
                finished_items = line.split("/")[-1].split("]")[0]
            if '\n' in line:

                each_section.append(line + ":" + (str(items_in_progress)))
                new_line_count += 1
            #    line = next(readFile)
            if '    ' in line:
                line = line.rsplit("    ")[-1].split('\n')[0]
            if '[x]' in line:
                complete_items += 1
            if '[x]' not in line:
                print(line)
            if ':' in line:
                section_complete_items = complete_items

                section_list.append(section_complete_items)
                section_complete_items = 0
                print(section_list)

            if '[]' in line:

                if ':' not in line:
                    items_in_progress += 1
            items_left = all_items - complete_items + 1


            all_items =  complete_items + items_in_progress
        print('Incomplete Items:',items_in_progress)
        print('Finished Items:',complete_items)
        print("Items Left:",items_left )
        print('Total Items:', all_items)



progress_scorer()