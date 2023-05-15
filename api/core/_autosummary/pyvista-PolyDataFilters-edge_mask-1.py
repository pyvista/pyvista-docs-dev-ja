# Plot the mask of points that exceed 45 degrees.
#
import pyvista
mesh = pyvista.Cube().triangulate().subdivide(4)
mask = mesh.edge_mask(45)
mesh.plot(scalars=mask)
#
# Show the array of masked points.
#
mask  # doctest:+SKIP
# Expected:
## array([ True,  True,  True, ..., False, False, False])
