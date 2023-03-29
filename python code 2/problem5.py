"""
Write a python function, find_pairs_of_numbers() which accepts a list of
positive integers with no repetitions and returns count of pairs of numbers
in the list that adds up to n.

The function should return 0, if no such pairs are found in the list.

Sample Input                              Expected Output

[1, 2, 7, 4, 5, 6, 0, 3]), 6            3 (1,5) (2,4)(6,0)

[3, 4, 1, 8, 5, 9, 0, 6], 9             4 (3,6) (4,5) (1,8) (9,0)
"""
def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n:
                count+=1
    return count
num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
num_list2=[3,4,1,8,5,9,0,6]
n2=9

print(find_pairs_of_numbers(num_list,n))
print(find_pairs_of_numbers(num_list2,n2))
