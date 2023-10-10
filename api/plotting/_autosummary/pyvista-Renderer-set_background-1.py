# Set the background color to black with a gradient to white at
# the top of the plot.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Cone())
pl.set_background('black', top='white')
pl.show()
