"""
string rotation
input: rhdt :246, ghftd:1246
Expl:here every string is associatted with the number sep by:
-->if sum of squares of digits is even then rotate the string by 1

-->if sum of squares of digits is odd is odd then rotate the string left by 2 position

2*2+4*4+6*6-56 which is even so rotate rhdt=trĥd

1 1+2 2+4 4+6*6-57 which is odd so rotate left by 2 :ghftd=ftdgh
"""
def sumSqrDigit(num):
    X = int(num)
    #rev = 1
    N = 0
    while(X>0):
        rev = X%10
        rev *= rev
        N += rev
        X = X//10
    return N
def rotateRight(string):
    n=''
    x=''
    n+=string[:-1]
    x+=string[-1]
    x+=n
    return x
def rotateLeft(string):
    n=''
    x=''
    n+=string[:2]
    x+=string[2:]
    x+=n
    return x
series = input().split(':')
for i in series:
    if(i.isdigit()):
        n=i
    else:
        stg=i
if(sumSqrDigit(n)%2==0):
    print(rotateRight(stg))
else:
    print(rotateLeft(stg))
