frequency = 500000000000000

if(frequency<=680000000000000 and frequency>620000000000000):
    colour = 'blue'
elif(frequency<=620000000000000 and frequency>600000000000000):
    colour = 'cyan'
elif(frequency<=600000000000000 and frequency>530000000000000):
    colour = 'green'
elif(frequency<=530000000000000 and frequency>500000000000000):
    colour = 'yellow'
elif(frequency<=500000000000000 and frequency>405000000000000):
    colour = 'red'
else:
    colour = 'black'

    
time = [0,1,2,3,4]
print(time)

# this seems like a very tedious task to fill a list
time = []
for i in range(5):
    time.append(i)
print(time)

# even shorter method using iterators
time = []
time = [i for i in range(5)]
print(time)

const = {"pi":3.14,"2pi":6.28,"pi2":1.57}

