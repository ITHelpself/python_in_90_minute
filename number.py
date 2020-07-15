# name = value
number = 5
print(number)
# additional two numbers
intVariable = 7
floatVariable = 6.3
subtractionResult = intVariable - floatVariable
print(subtractionResult)
multipleResult = intVariable * floatVariable
divisionResult = intVariable / floatVariable
modulusResult = intVariable % 3
# number coversion
intNumber = 3
stringIntNumber = "4"
testSum = intNumber * int(stringIntNumber)
print(testSum)
# global variable
global variable
variable = 5
print(variable)
# function
globalX = 5
def addOne(x):
    global globalX
    y = x+1
    y = globalX + 1
    return y
startNumber = -1
nextNumber = addOne(startNumber)
print(nextNumber)
# if...elseif... else
testVariable = 10
if testVariable <10:
    print("value less than 10")
elif testVariable == 10:
    print("value more than 10")
else:
    print("value greater than 10")
