def findGuest(guests, N):
    count = 0
    for i in range(N):
        if guests[i] <= count:
            count += 1
    return count


guests = []
N = int(input("Enter total number of guests"))
for i in range(N):
    x = int(input("Enter the requirement of the guest : "))
    guests.append(x)
totalGuests = findGuest(guests, N)
print(totalGuests)
