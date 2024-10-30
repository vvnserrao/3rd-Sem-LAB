import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,2,3,4,5]

plt.plot(x,y1,marker='o',c='r',label='y = x^2')
plt.plot(x,y2,marker='x',c='g',label='y = x')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Multiple Lines on Same Plot')
plt.legend()
plt.grid(True)