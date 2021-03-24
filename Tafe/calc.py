# - Brendan McCann
# - 17/03/21
# - Simple calculator with input validation

def testInput(x,isOper = False):
    while True:
	
    #Operator test
        if isOper == True:
            validOps = ['+','-','*','/']
            if x in validOps:
                return x
            else:
                x = input("\nValid operators are +, -, *, or /\nPlease specify operator: ")
                return testInput(x,True)

    #Number test
        try:
            x = float(x)
        except ValueError:
            x = input("Invalid input, please try again: ")
        else:
            if float(x).is_integer():
                x = int(x)
            else:
                x = round(float(x),2)
            print(f'{x:,} Accepted')
            return x

def calc(x,y,z):
    if z == "+":
        return x+y
    elif z == "-":
        return x-y
    elif z == "*":
        return x*y
    else:
        return x/y
      
num1 = testInput(input("Please enter number 1: "))
num2 = testInput(input("\nPlease enter number 2: "))

oper = testInput(input("\nValid operators are +, -, *, or /\nPlease specify operator: "),True)

ans = round(calc(num1,num2,oper),2)

print("\n{0:,} {1} {2:,} = {3:,}".format(num1,oper,num2,ans))
