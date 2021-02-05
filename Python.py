import numpy as np
from matplotlib import pyplot as plt



x = np.linspace(0,7,100)
y = np.sin(x)



fig, ax = plt.subplots(1,1)

ax.plot(x,y,"r-")
ax.set_xlabel("Angulo")
ax.set_ylabel("Seno")
ax.set_title("Representación de la Función Seno")



