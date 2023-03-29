"""Write python function, nearest palindrome) which accepts a number and returns the nearest
palindrome greater than the given number.

Sample input   Expected Output

 99                101
1221               1331"""
import sys
def next_nearest_palindrome(num):
    numstr=str(num)
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(next_nearest_palindrome(99))
print(next_nearest_palindrome(1221))
print(next_nearest_palindrome(1250 ))
print(sys.maxsize)


    
    



