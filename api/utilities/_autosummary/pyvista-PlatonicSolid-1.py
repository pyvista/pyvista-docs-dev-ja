# Create and plot a dodecahedron.
#
import pyvista as pv
dodeca = pv.PlatonicSolid('dodecahedron')
dodeca.plot(categories=True)
