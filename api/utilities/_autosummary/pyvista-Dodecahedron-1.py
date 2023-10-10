# Create and plot a dodecahedron.
#
import pyvista as pv
tetra = pv.Dodecahedron()
tetra.plot(categories=True)
