# Create and plot a dodecahedron.
#
import pyvista as pv
dodeca = pv.PlatonicSolidSource('dodecahedron')
dodeca.output.plot(categories=True)
