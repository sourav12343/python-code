"""Write a python program to display all the common characters between two strings.
Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any.

Perform case sensitive string comparison wherever necessary.
Sample Input                  Expected Output
"I like Python"
"Java is very popular language"   lieyon"""
sentence1="I like Python"
sentence2="Java is very popular language"
x=""
for i in sentence1:
  for j in sentence2:
      if i==j and i!=" ":
          x=x+i
          break
print(x)
