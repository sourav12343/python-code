"""
Given a number n, write a program to find the sum of the largest prime factors
of each of nine consecutive numbers starting from n.

g(n) = f(n)+ f(n+1)+ f(n+2)+ f(n+3)+ f(n+4)+ f(n+5)+ f(n+6) +f(n+7) f(n+8)

where, g(n) is the sum and f(n) is the largest prime factor of n

For example,

(10)-f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
=5+11 + 3 + 13+ 7+ 5+ 2+ 17+ 3 
=66
"""
def find_factors(num):
        factors = []
        for i in range(2,(num+1)):
            if(num%i==0):
                factors.append(i)
        return factors
def is_prime(num, i):
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))
def find_largest_prime_factor(list_of_factors):
    large=[]
    for i in list_of_factors:
        if is_prime(i,i//2)==True:
            large.append(i)
    return max(large)
def find_f(num):
    f=find_factors(num)
    l=find_largest_prime_factor(f)
    return l
def find_g(num):
    sum=0
    consicutive=[i for i in range(num,num+9)]
    for i in consicutive:
        largest_prime_factor=find_f(i)
        sum=sum+largest_prime_factor
    return sum
print(find_g(10))
