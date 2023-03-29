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
