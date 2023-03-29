#problem3 flight ticket
"""The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
Rate per Adult: Rs. 37550.0
Rate per Child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers) As it was a holiday season,
the airline also offered 10% discount on the final ticket cost (after inclusion of the
service tax). Find and display the total ticket cost for a group which had adults and
children.

Test the program with different input values for number of adult and children
          Sample Input                                  Expected Output 
Number of adults     Number of children
5                     2                           Total Ticket Cost: 204910.35
3                     1                           Total Ticket Cost: 120535.5 """ 

adult=int(input("enter no. of adults"))
child=int(input("enter no. of child"))
total=((adult*37550.0)+(child*37550*0.33))
print("Total",total)
total1=total*0.07
total2=total+total1
print("with service tax",total2)
total3=total2*0.90
print("with discount",total3)
