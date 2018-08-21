line_location = []
def countLines():
    count_lines = 0
    with open('scroll.glif', 'r') as readFile:
       # n = [line for line in readFile if '!' and 'var' in line]
        #print(n)
        for lines in readFile:
            count_lines += 1
            count_lines_and_line_data = count_lines, lines
            if '\n' in count_lines_and_line_data:
                count_lines_and_line_data = str(count_lines_and_line_data).split("\n")[0]
            line_location.append(count_lines_and_line_data)
        for i in line_location:
            pass
    #        line_location.append(i)
    for i in range(len(line_location)):
        pass
    #    print(line_location[i])
   # print(line_location)
countLines()