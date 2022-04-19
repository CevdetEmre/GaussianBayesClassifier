import numpy as np
import matplotlib.pyplot as plt


mean1 = 10
mean2 = -10
variance = 1

def createXAxis(mean,variance):
    return np.random.normal(mean,variance,(400,1))

def createYAxis(mean,variance):
    return np.random.normal(mean*2,variance*3,(400,1))

def GaussianBayesClassification(radius,center=(0, 0),number_of_points=100):
    center_x, center_y = center
    r = radius * np.sqrt(np.random.random((number_of_points,)))
    theta = np.random.random((number_of_points,)) * 2 * np.pi
    x = center_x + r * np.cos(theta)
    y = center_y + r * np.sin(theta)
    return x, y



 
X = np.arange(-20, 20)
fig, ax = plt.subplots()

X1 = createXAxis(mean1,variance)
X2 = createXAxis(mean2,variance)
# define the y co-ordinates
Y1 = createYAxis(mean1,variance)
Y2 = createYAxis(mean2,variance)
ax.scatter(X1,Y1,c="orange",label="oranges")
ax.scatter(X2,Y2,c="y",label="lemons")

ax.plot(X, 0.9 * X, "g-", linewidth=2)

ax.legend()
ax.grid()
plt.show()