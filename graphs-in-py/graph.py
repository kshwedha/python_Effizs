import matplotlib.pyplot as plt
x=[1,6,2,4,9,4]
y=[9,2,5,0,3,1]

plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
#plt.plot([1,2,3])
#plt.plot(x,y, label="1")

#tick_label = ['one', 'two', 'three', 'four', 'five']
#plt.bar(x,y, tick_label = tick_label, width = 0.8, color = ['red', 'green']) 

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('whatever')

plt.show()
