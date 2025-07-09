import matplotlib.pyplot as plt
import numpy as np

# Define the heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Plot the heart shape
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='red')



#  parameters
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.axis('off')  # Turn off axis
plt.gca().set_aspect('equal')  # Ensure the aspect ratio is equal

# Display
plt.show()
