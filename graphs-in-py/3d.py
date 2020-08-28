from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np 

# setting a custom style to use 
style.use('ggplot') 

# create a new figure for plotting 
fig = plt.figure() 

# create a new subplot on our figure 
# and set projection as 3d 
ax1 = fig.add_subplot(111, projection='3d') 

# defining x, y, z co-ordinates 
x = np.random.randint(0, 10, size = 20) 
y = np.random.randint(0, 10, size = 20) 
z = np.random.randint(0, 10, size = 20)  


# setting labels for the axes 
ax1.set_xlabel('x-axis') 
ax1.set_ylabel('y-axis') 
ax1.set_zlabel('z-axis') 

#plotting poins to scatter
ax1.scatter(x, y, z, c = 'm', marker = 'o')

# function to show the plot 
plt.show()

# defining a, b, c co-ordinates 
a = np.random.randint(0, 10, size = 5) 
b = np.random.randint(0, 10, size = 5) 
c = np.random.randint(0, 10, size = 5) 

ax2=fig.add_subplot(111, projection='3d')

# plotting the points on subplot
ax2.plot_wireframe(a,b,c)

plt.show()

