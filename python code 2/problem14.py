"""Input: a string of comma seperated numbers. the number 5 and 8 are present in
the list. Assume that 8 always comes after 5.
casel:numl= add all the numbers which do not lie between 5
and 8 in the input
case2:num2 =number formed by concatenating all numbers from 5 to 8

output sum of numl and num2

example

1) 3,2,6,5,1,4,8,9

num1=3+2+6+9=20

num2=5148
o/p-5148+20=5168"""
ara = list(map(int,input().split(",")))
num1 = sum(ara[:ara.index(5)])+sum(ara[ara.index(8)+1:])
print(num1)
l = ara[ara.index(5):ara.index(8)+1]
#print(l)
num2 = ""
for i in l:
    num2+=str(i)
#print(num2)
print(int(num2)+num1)
