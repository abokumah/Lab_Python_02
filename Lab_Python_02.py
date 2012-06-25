"""1.
x=2
nothing
x=1
z=7
"""
"""2.
y=1
y=1
"""
"""3.
2,4,6,8,10
"""
"""4.
nothing
"""
#6.
primarySchoolAge = 4
votingAge = 18
presidentialAge = 40
retirementAge = 60
personsAge = input ("Enter an age:")
if personsAge < primarySchoolAge:
    print "Too Young"
if personsAge > votingAge:
    print "Remeber to vote"
if personsAge > presidentialAge:
    print "Vote for me"
elif personsAge < presidentialAge and personsAge > retirementAge:
    print "You can't be president"
if personsAge > retirementAge:
    print "Too old"
else:
    print"Your age does not fall into a category"

#7.

i= 40
while i>=0:
    j= i*3
    if j<40:
        print j
    i= i-1

#8.
for i in range (6,30,1):
    if i % 2 != 0:
        if i% 3 != 0:
            if i % 5 != 0:
                print i

#9.
n = 0
while ((79*n) % 97) != 1:
    
    n = n+1
print n
   
