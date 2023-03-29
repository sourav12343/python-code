"""
Write a python function, check_double (number) which accepts a whole number
and returns True if it satisfies the given conditions.

1. The number and its double should have exactly the same number of digits.

2. Both the numbers should have the same digits, but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the
same digits, but in a different order.
"""
def check_double(number):
    list1 = [int(x) for x in str(number)]
    list2 = [int(x) for x in str(number*2)]
    list3 = sorted(list1)
    list4 = sorted(list2)
    if list3 == list4 and list1 != list2:
        return True
    else:
        return False

print(check_double(125874))
print(check_double(1248))
