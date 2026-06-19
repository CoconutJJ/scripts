# render_gnomonic.py  (run once, outputs gnomonic.svg)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

# Sphere wireframe
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_wireframe(xs, ys, zs, color="steelblue", alpha=0.2, linewidth=0.5)

# Tangent plane at north pole (z=1)
px = np.linspace(-0.5, 0.5, 2)
py = np.linspace(-0.5, 0.5, 2)
PX, PY = np.meshgrid(px, py)
# PZ = np.ones_like(PX) * 3.0
ax.plot_surface(
    PX, PY, PX - PY + 2, alpha=0.3, color="orange"
)

# 0.5 * PX + 0.5 * PY + 0.5 * PZ = 0

# (n - p) * v =  0 
# (n * v - p * v) = 0

# Gnomonic rays: from center (0,0,0) through points on sphere to plane
for theta in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    for phi in [np.pi / 6, np.pi / 4]:
        # Point on sphere
        sx = np.sin(phi) * np.cos(theta)
        sy = np.sin(phi) * np.sin(theta)
        sz = np.cos(phi)
        # Project to plane z=1: scale so z=1

        # t = 0.33 / sz
        # px_, py_, pz_ = t*sx, t*sy, 1.0
        # ax.plot([0, px_], [0, py_], [0, pz_], 'r-', alpha=0.6, linewidth=0.8)
        # ax.scatter([sx], [sy], [sz], color='red', s=10)
        # ax.scatter([px_], [py_], [pz_], color='darkred', s=10, marker='^')

# Center of projection
ax.scatter([0], [0], [0], color="black", s=40, zorder=5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Gnomonic Projection")
ax.set_box_aspect([1, 1, 1])
ax.set_aspect("equal")
plt.tight_layout()
plt.savefig("gnomonic.svg", format="svg", bbox_inches="tight")
