import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.02)
y1 = 10*np.sin(x)+10*np.cos(x)
y2 = 15*np.sin(x)+15*np.cos(x)
y3 = 30*np.sin(x)+30*np.cos(x)

plt.plot(x, y1, label = "(10,10)")
plt.plot(x, y2, label = "(15,15)")
plt.plot(x, y3, label = "(30,30)")
plt.legend()
plt.title("Q2.4 Hough Space Plot")
plt.xlabel("theta")
plt.ylabel("rho")
plt.grid(True)
plt.xlim(0,2*np.pi)
plt.show()