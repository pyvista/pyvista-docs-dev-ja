# Create and plot an octahedron.
#
import pyvista as pv
tetra = pv.Octahedron()
tetra.plot(categories=True)
