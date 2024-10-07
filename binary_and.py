# binary operators and,or,not
#and is a logical binary operator if both the values are true then returns true if anyone is wrong 
#returns false an example is shown below
num=int(input('enter the number'))
if(num%3==0 and num%5==0):
    print('The number is divisible by both 3 and 5')
else:
    print('the number is not divisible by both 3 and 5')

