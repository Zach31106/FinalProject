#Louis part
import math
class functions:
    def __init__(self, functionList, inputValue):
        self.functionList = functionList
        self.inputValue = inputValue
#def rational(f, g):
#    return f / g
#def exponential(c, f):
#    return math.exp(f * math.log(c, math.e))
#def cosine(f):
#    return math.cos(f)
#def addition(f, g):
#    return f + g
#def subtraction(f, g):
#    return f - g
#def bracketSort(func):  #this section is useless unless we use strings but im keeping it here bc why not
    #bracketPositions = []
    #for i in range(len(func)):
        #if func[i] == "(":
            #brackets.append("(")
            #bracketPositions.append(i)
        #if func[i] == ")":
            #brackets.append(")")
            #bracketPositions.append(i)
    #newfuncs = []
    #for j in range(len(brackets)):
        #if brackets[j] == "(" and brackets[j+1] == ")": # we have a fully nested bracket pair
            #brackets[j+1:] = brackets[j+1:][::-1]
listFunction = []
def inputReceiver(inputButton):
    newInputList = []
    parenthesesOrder = []
    if inputButton == "sinx":
        newInputList.append("sine")
    if inputButton == "cosx":
        newInputList.append("cosine")
    if inputButton == "+":
        newInputList.append("plus")
    if inputButton == "-":
        newInputList.append("minus")
    if inputButton == "*":
        newInputList.append("times")
    if inputButton == "/":
        newInputList.append("divided")
        newInputList.append("openPar")
        parenthesesOrder.append("reg")
    if inputButton == "lnx":
        newInputList.append("natLog")
    if inputButton == "(":
            newInputList.append("openPar")
            parenthesesOrder.append("reg")
    if inputButton == ")":
        if parenthesesOrder[-1] == "reg":
            newInputList.append("closePar")
            parenthesesOrder.pop()
        else:
            newInputList.append("endPow")
            parenthesesOrder.pop()
    if inputButton == "^":
        newInputList.append("pow")
        parenthesesOrder.append("exp")





def inputBuilder(funcList, inputList, command):
     x=1 #get rid of error message



