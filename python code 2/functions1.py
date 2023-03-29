#categories of functions
#based on arguments
#1.positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
#function1(3,4,5,)    here  number required and we gave 3 so error
#function1(1,2,3,4,5)  here 4  number required and we gave 5 so error


#2.keyword arguments
def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=20,num3=10,num1=40,num2=60)
#3.default arguments
def function3(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("anshuman",335,"Cse")
function3("Jyoti",338,"Cst")
function3("vinod",353)
function3("tushar",345,"eee")
#4. variable number of arguments
def function4(*var):
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50)
print()
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50))

 
