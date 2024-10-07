salary=int(input('Enter the salary:'))
age=int(input('enter the age:'))
if(salary>=20000 or age<=25):
    loan_amount=int(input('Enter the required the loan amt:'))
    if(loan_amount>=50000):
        print("maaximum loan amount is 50000")
    else:
     print('you are elgibile for loan')
else:
    print("you are not elgiile for loan")
