"""
Find the number of distinct subarrays in an array of position integers such
that the sum of the subarray is an odd integer, two subarray are consisdered
different if they start or end at different index input.

1
3
123 
[1] [12] [1,2,3] [2] [2,3] [3] [13]
 4
"""
l = int(input())
h = int(input())
l1 = []
c=0
for i in range(l,h+1):
    l1.append(i)  
for i in range(len(l1)+1):
    for j in range(i):
        if sum(l1[j:i])%2!=0:
            c+=1
print(c)
