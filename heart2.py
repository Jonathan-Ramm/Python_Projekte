import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Herzfunktion 
def heart_function(k):
    x = 16 * np.sin(k)**3
    y = 13 * np.cos(k) - 5 * np.cos(2*k) - 2 * np.cos(3*k) - np.cos(4*k)
    return x, y

# Werte für k
k = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_function(k)

# Figur und Achsen erstellen
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.axis('off')

# Initialisierungsfunktion
def init():
    line.set_data([], [])
    return line,

# Animationsfunktion
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,


line, = ax.plot([], [], 'r-', lw=2)

# Animation erstellen
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(k), interval=20, blit=True, repeat=False)

plt.title('Herz')
plt.show()
