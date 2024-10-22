#WAP to find greatest of 3 numbers entered by the user 
a =float(input("enter 1st number :"))
b =float(input("enter 2nd number :"))
c =float(input("enter 3rd number :"))

if(a > b and a > c):
    print("A is greatest")
elif(b > a and b > c):
    print("B is greatest")
elif(c > a and c > b):
    print("C is greatest")
else:
    print("you entered same number or a string")
