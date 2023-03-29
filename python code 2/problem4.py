"""Write a python function which accepts a sentence and finds the number of
letters and digits in the sentence. It should return a list in which the first
value should be letter count and second value should be digit count. Ignore
the spaces or any other special character in the sentence.

Sample Input            Expected Output
Infosys 123               [7,3]
ABCEFG                    [6,0]
"""
def fun(str1):
    count1=0
    count2=0
    l=[]
    for i in str1:
        if i.isalpha():
            count1=count1+1
        elif i.isdigit():
            count2=count2+1
        else:
            continue
    return[count1,count2]
print(fun("Anshuman 123"))
print(fun(" 123"))
print(fun("Anshuman #"))
