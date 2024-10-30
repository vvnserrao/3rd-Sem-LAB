import matplotlib.pyplot as plt
x=[]
y=[]

with open("Test.txt", "r") as file:
    for line in file:
        part=line.split()
        if len(part) == 2:
            x.append(int(part[0]))
            y.append(int(part[1]))

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot with Labels and Title')
plt.plot(x, y);