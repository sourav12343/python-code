"""
Write a python function to add 'ing' at the end of a given string and return
the new string.

If the given string already ends with 'ing' then add "ly".

If the length of the given string is less than 3, leave it unchanged.

Sample Input              Expected Output
sleep                       sleeping
amazing                     amazingly
is                           is
"""
def fun(str):
  if len(str) < 3:
    return str
  elif str[-3:]=="ing":
      return str+"ly"
  else:
        return str+"ing"


print(fun('sleep'))
print(fun('amazing'))
print(fun('is'))

