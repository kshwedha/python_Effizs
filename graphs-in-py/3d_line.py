# importing required modules 
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np 

# setting a custom style to use 
style.use('ggplot') 

# create a new figure for plotting 
fig = plt.figure() 

# create a new subplot on our figure 
ax1 = fig.add_subplot(111, projection='3d') 

# defining x, y, z co-ordinates 
x = np.random.randint(0, 10, size = 5) 
y = np.random.randint(0, 10, size = 5) 
#z1= np.random.randint(0, 10, size = 5)
import random
z1=[random.randint(0,10) for i in range(5)]
z=np.array([z1,z1])
#import random
#z=np.array([random.randint(0, 10, size= 5)],[random.randint(0, 10, size= 5)])
# plotting the points on subplot 

ax1.plot_wireframe(x,y,z) 

# setting the labels 
ax1.set_xlabel('x-axis') 
ax1.set_ylabel('y-axis') 
ax1.set_zlabel('z-axis') 

plt.show()

