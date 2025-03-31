#Simple matplotlib demo
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,101)
plt.plot(x, np.sin(x),'b.')
plt.plot(x, np.cos(x),'r-.')
plt.show()
