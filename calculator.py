import re

def mysplit(mystr):
    return re.split("([+-/*//%])", mystr.replace(" ", ""))
   
class calculator:
    def add(x,y):
        sum = x + y
        print(sum)
       
    def sub(x,y):
        diff = x - y
        print(diff)

    def mul(x,y):
        prod = x * y
        print(prod)

    def div(x,y):
        quo = x / y
        print(quo)
   
    def modulus(x, y):
        mod = x % y
        print(mod)
   
    def mulfl(x, y):
        prodf = x//y
        print(prodf)
       
exp = input("Enter the expression")
exp=mysplit(exp)

for i in exp:
    if i == '+':
        calculator.add(int(exp[0]), int(exp[2]))
    elif i == '-':
        calculator.sub(int(exp[0]), int(exp[2]))
    elif i == '*':
        calculator.mul(int(exp[0]), int(exp[2]))
    elif i == '//':
        calculator.mulfl(int(exp[0]), int(exp[2]))
    elif i == '/':
        calculator.div(int(exp[0]), int(exp[2]))
    elif i == '%':
        calculator.modulus(int(exp[0]), int(exp[2]))
   
print("Thank You")