class Generator:

    # Arguments are ordered this way since in Python arguments with default values can't be placed
    # prior to arguments without default values. This is because the Python interpreter won't know
    # what argument you're passing if the default value arguments were prior.
    def __init__(self, numAmt, endNum, startNum=0, addNumAmts=False, repeatNum=True):
        #Int - total number of integers in the combination
        self.numAmt = numAmt
        #Int
        self.endNum = endNum
        #Int
        self.startNum = startNum
        #Bool - Add combinations with integer count less than numAmt
        self.addNumAmts = addNumAmts
        #Bool - Use repeating numbers in combination
        self.repeatNum = repeatNum

    def generateCombinations():
        combinationList = []
        currentCombination = []

        for i in numAmt:
            currentCombination.append(startNum)
        return currentCombination
