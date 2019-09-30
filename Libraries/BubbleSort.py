##This function returns the list in the ascending order from the lowest to maximum number
def getSortedList(inputList=[]):
    for i in range(0,len(inputList)-1):
        for j in range(0,len(inputList)-1):
            currentNum,nextNum = inputList[j],inputList[j+1]
            if currentNum > nextNum:
                inputList.remove(currentNum)
                inputList.insert(j+1,currentNum)

    return inputList
