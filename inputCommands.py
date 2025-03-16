#Louis part
class variable:
    def __init__(self, type):
        self.type = type
x = variable("independent")
import math
def rational(f, g):
    return f / g
def exponential(c, f):
    return math.exp(f * math.log(c, math.e))
def cosine(f):
    return math.cos(f)
def addition(f, g):
    return f + g
def subtraction(f, g):
    return f - g
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
    if inputButton == "sinx":
        newInputList.append(math.sin(x))
    if inputButton == "cosx":
        newInputList.append(math.cos(x))
    if inputButton == "*":
        inputBuilder(listFunction, newInputList, "append")
        newInputList = []
    if inputButton == "(":




def inputBuilder(funcList, inputList, command):
    if



