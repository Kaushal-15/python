#if we use the keyword Exception then every error will be handled if we specify the error then it will only be catched 
try:
    a=int(input())
    b=int(input())
    c=input()#here i would give input as 20 or any other integer then it will be type error then run time error will occur as the exception is only for valueError
    print(c/a)
except ValueError as e:
    print(e)
finally:
    print("Done")#if the code as error or not the finally keyword will auomatically execute after the execution of the try and except block
