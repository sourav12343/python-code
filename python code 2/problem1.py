"""wap to find and display the product of three positive integer values based on the rules
mentioned below.
it should display the product of the three values except when one of the integer value is 7.
in that case ,7 should not be include in the product and the values to its left also should
not be included.
if there is only one value to be considered,display the value itself.
if no values can be included in the product,display -1
Note: Assume that if 7is one of the positive integer values,then it will occur only once.
Refer the Sample I/o given below
sample input     Expected output
2,5,3            30
7,4,3            12
5,7,6             6
3,2,7            -1
"""
num1=int(input())
num2=int(input())
num3=int(input())
if num1==7:
    print(num2*num3)
elif num2==7:
    print(num3)
elif num3==7:
    print(-1)
else:
    print(num1*num2*num3)

