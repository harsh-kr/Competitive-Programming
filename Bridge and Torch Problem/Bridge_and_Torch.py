''' Four people come to a river in the night.
There is a narrow bridge, but it can only hold two people at a time.
They have one torch and, because it's night, the torch has to be used when crossing the bridge.
Person A can cross the bridge in 1 minute, B in 2 minutes, C in 5 minutes, and D in 8 minutes.
When two people cross the bridge together, they must move at the slower person's pace.
The question is, can they all get across the bridge in 15 minutes or less?
'''

personTime={'A':1, 'B':2, 'C':5, 'D':8}
totalTime = 15
timeSpent = 0

# sorting the time values from dictionary
orderTime = list(personTime.values())
orderTime.sort()
for k, v in personTime.items():
    if v == orderTime[3]:
        p4 = k
    elif v == orderTime[2]:
        p3 = k
    elif v == orderTime[1]:
        p2 = k
    elif v == orderTime[0]:
        p1 = k

# strategy used for solving
# bridge and torch problem

print('First ' + p1 + ' and ' + p2 + ' spend ' + str(orderTime[1]) + ' of total ' + str(totalTime) + ' min.')
timeSpent += orderTime[1]

print('Then person ' + p1 + ' will return spending ' + str(orderTime[0]) + ' min thus making total time spent ' + str(timeSpent+orderTime[0]) + ' min')
timeSpent += orderTime[0]

print('Now ' + p3 + ' and ' + p4 + ' cross the bridge spending ' + str(orderTime[3]) + ' min thus making total time spent ' + str(timeSpent+orderTime[3]) + ' min')
timeSpent += orderTime[3]

print('Now ' + p2 + ' returns to get person ' + p1 + ' spending ' + str(orderTime[1]) + ' min thus making total time spent ' + str(timeSpent+orderTime[1]) + ' min')
timeSpent += orderTime[1]

print('Finally person ' + p1 + ' and ' + p2 + ' join their friends on the other side, spending another ' + str(orderTime[1]) + ' min and if we add that to ' + str(timeSpent) + ' min already spent, that makes it ' + str(timeSpent+orderTime[1]) + ' min in total.')