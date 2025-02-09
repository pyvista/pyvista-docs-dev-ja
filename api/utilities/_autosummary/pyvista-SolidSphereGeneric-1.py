# Linearly sampling spherical coordinates does not lead to
# cells of all the same size at each radial position.
# Cells near the poles have smaller sizes.
#
import pyvista as pv
import numpy as np
solid_sphere = pv.SolidSphereGeneric(
    radius=np.linspace(0, 0.5, 2),
    theta=np.linspace(180, 360, 30),
    phi=np.linspace(0, 180, 30),
)
solid_sphere = solid_sphere.compute_cell_sizes()
solid_sphere.plot(scalars='Volume', show_edges=True, clim=[3e-5, 5e-4])
#
# Sampling the polar angle in a nonlinear manner allows for consistent cell volumes.  See
# `Sphere Point Picking <https://mathworld.wolfram.com/SpherePointPicking.html>`_.
#
phi = np.rad2deg(np.arccos(np.linspace(1, -1, 30)))
solid_sphere = pv.SolidSphereGeneric(
    radius=np.linspace(0, 0.5, 2),
    theta=np.linspace(180, 360, 30),
    phi=phi,
)
solid_sphere = solid_sphere.compute_cell_sizes()
solid_sphere.plot(scalars='Volume', show_edges=True, clim=[3e-5, 5e-4])
