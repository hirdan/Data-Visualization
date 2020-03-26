# loading matplotlib library
import matplotlib.pyplot as plt
x=[2,9,3,7]
y=[7,15,5,9]
plt.xlabel('Distance')  # x-axis
plt.ylabel('Time')   #y-axis
plt.plot(x,y,label='railway track') #this will draw a line
plt.scatter(x,y,s=200,label='railway station',marker='*',color='red') #this will draw points of size 200mm
plt.bar(x,y,label='height of railway station') #this will draw bars
plt.grid(color='green') #this will draw a grid
plt.legend() #it will show label in the plot
plt.show()  #it wil draw the graph
