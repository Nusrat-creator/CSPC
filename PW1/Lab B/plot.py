import numpy as np
import matplotlib.pyplot as plt

t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)

LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed, color='blue', label='Observed Data', s=15)
ax1.set_title('Observed Data')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('Count (N)')
ax1.grid(True)

ax2.plot(t, analytical, color='red', label='Analytical Curve')
ax2.set_title('Analytical Law')
ax2.set_xlabel('Time (t)')
ax2.grid(True)

plt.tight_layout()

plt.savefig('figure.png')
print("figure.png saved successfully.")
