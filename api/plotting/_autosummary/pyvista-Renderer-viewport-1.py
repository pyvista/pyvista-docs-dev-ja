# Show the viewport of a renderer taking up half the render
# window.
#
import pyvista as pv
pl = pv.Plotter(shape=(1, 2))
_ = pl.add_mesh(pv.Sphere())
pl.renderers[0].viewport
# Expected:
## (0.0, 0.0, 0.5, 1.0)
#
# Change viewport to half size.
#
pl.renderers[0].viewport = (0.125, 0.25, 0.375, 0.75)
pl.show()
