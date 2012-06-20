print "Please provide us with your date of birth using this format"
Month = input('Month(The Value e.g. enter 1 to represent Jan):') - 2
if Month <= 0:
    Month = Month + 12

Day = input('Day of the month:')

Year = input('Year e.g. 89:')
Century = input('Century e.g. 19:')

W = (13*Month - 1)/5
X = Year/4
Y = Century/4

Z = W + X + Y + Day + Year - 2*Century
R = Z%7

if R < 0:
    R = R + 7
    if R == 0:
        print "Sunday"
    elif R == 1:
        print "Monday"
    elif R == 2:
        print "Tuesday"
    elif R == 3:
        print "Wednesday"
    elif R == 4:
        print "Thursday"
    elif R == 5:
        print "Friday"
    elif R == 6:
        print "Saturday"


elif R == 0:
    print "Sunday"
elif R == 1:
    print "Monday"
elif R == 2:
    print "Tuesday"
elif R == 3:
    print "Wednesday"
elif R == 4:
    print "Thursday"
elif R == 5:
    print "Friday"
elif R == 6:
    print "Saturday"
    



