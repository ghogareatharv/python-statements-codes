a=int(input("enter the number\n"))
b=int(input("enter the first number by which you want to divide\n"))
c=int(input("enter the secound number by which you want to divide\n"))
if(a%b==0 and a%c==0):
    print(a,"is divisible by",b,"and",c)
else:
    print(a,"is not divisible by",b,"and",c)