import numpy as np
import matplotlib.pyplot as plt

n = 900
x = np.linspace(-12, 12, n)
y = np.linspace(-12, 12, n)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2) + 1e-9
Theta = np.arctan2(Y, X)
pi = np.pi

field_1 = np.sin(2 * pi * R / 3.6)
field_2 = 0.75 * np.sin(2 * Theta + 2 * pi * R / 8.0)

Xr1 = 0.92 * X + 0.35 * Y
Yr1 = -0.25 * X + 1.08 * Y
R1 = np.sqrt(Xr1**2 + Yr1**2) + 1e-9
field_3 = 0.55 * np.cos(2 * pi * R1 / 5.2)

field_4 = 0.35 * np.sin(4 * Theta - R / 1.7)
stabilizer = np.exp(-(R**2) / 55.0)

Z = (field_1 + field_2 + field_3 + field_4) * stabilizer

fig, ax = plt.subplots(figsize=(8, 8), dpi=180)
ax.imshow(
    Z,
    extent=[x.min(), x.max(), y.min(), y.max()],
    origin="lower",
    interpolation="bilinear"
)
levels = np.linspace(Z.min() * 0.7, Z.max() * 0.7, 12)
ax.contour(X, Y, Z, levels=levels, linewidths=0.6)
ax.set_title("Simulation π_field: Orbital Continuity")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal")
plt.show()
