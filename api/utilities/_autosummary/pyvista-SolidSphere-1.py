# Create a solid sphere.
#
import pyvista as pv
import numpy as np
solid_sphere = pv.SolidSphere()
solid_sphere.plot(show_edges=True)
#
# A solid sphere is 3D in comparison to the 2d :func:`pyvista.Sphere`.
# Generate a solid hemisphere to see the internal structure.
#
isinstance(solid_sphere, pv.UnstructuredGrid)
# Expected:
## True
partial_solid_sphere = pv.SolidSphere(
    start_theta=180, end_theta=360
)
partial_solid_sphere.plot(show_edges=True)
#
# To see the cell structure inside the solid sphere,
# only 1/4 of the sphere is generated. The cells are exploded
# and colored by radial position.
#
partial_solid_sphere = pv.SolidSphere(
    start_theta=180,
    end_theta=360,
    start_phi=0,
    end_phi=90,
    radius_resolution=5,
    theta_resolution=8,
    phi_resolution=8,
)
partial_solid_sphere["cell_radial_pos"] = np.linalg.norm(
    partial_solid_sphere.cell_centers().points, axis=-1
)
partial_solid_sphere.explode(1).plot()
