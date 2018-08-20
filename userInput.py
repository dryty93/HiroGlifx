# this is an early implementation of the user input function. it is being
# edited for better readability and performance.

def ui(userInput):
    from variable import varDict

    global prompt
    global promptVal
    global promptVar
    global prompted

    prompt = input(userInput)
    prompted = promptVar[0]
    print(prompt)
    varDict[prompted] = prompt


def uIOut():
    from main import StartInterpret

    global line
    global finalPrompt
    global promptVar
    global uiAnswer

    line = StartInterpret.line
    promptSeq = line.split('UI')
    promptJOin = ''.join(promptSeq)
    fPrompt = promptJOin.split('(')
    lPrompt = ''.join(fPrompt)
    fPromptW = lPrompt.split(')')
    finalPrompt = ''.join(fPromptW)
    promptVar = finalPrompt.split('$=')
    finPromptVar = ''.join(promptVar)
    dividerPrompt = finPromptVar.split('^')
    last = dividerPrompt[-1]
    ui(last)
