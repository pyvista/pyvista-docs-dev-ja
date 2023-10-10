# Create and plot an icosahedron.
#
import pyvista as pv
tetra = pv.Icosahedron()
tetra.plot(categories=True)
