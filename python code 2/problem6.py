"""
Write a Python function which accepts a string and returns a string made of
the first 2 and the last 2 characters of the given string. If the string
length is less than 2, return -1.

Note: If the string length is equal to 2, consider the 2 characters to
be the first as well as the last two characters.

Sample Input                 Expected Output.
w3resource                      w3ce
w3                              w3w3
A                                -1
"""
def string_both_ends(str):
  if len(str) < 2:
    return '-1'

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

