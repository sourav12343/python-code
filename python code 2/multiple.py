#read a number and check if it is multiple of 3 or 5 or both else invalid
n=int(input("enter a number"))
if n%3==0 and n%5!=0:
    print("multiple of 3");
elif n%5==0 and n%3!=0:
    print("multiple of 5")
elif n%3==0 and n%5==0:
    print("multiple of both")
else:
    print("invalid")
