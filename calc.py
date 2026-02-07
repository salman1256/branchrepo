def add(num1, num2):
    return num1+num2
def multi(num1, num2):
    return num1*num2
def sub(num1, num2):
    return num1-num2
def div(num1, num2):
    return num1/num2

print('Calculator Example')

fnum=float(input( 'enter first number: '))
snum=float(input( 'enter second number: '))
print ('Result after addition: ',add(fnum,snum))