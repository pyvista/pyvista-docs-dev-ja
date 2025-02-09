# Set the logo file to a custom logo.
#
import pyvista as pv
from pyvista import examples
logo_file = examples.download_file('vtk.png')
pv.global_theme.logo_file = logo_file
#
# Now the logo will be used by default for :func:`pyvista.Plotter.add_logo_widget`.
#
pl = pv.Plotter()
_ = pl.add_logo_widget()
_ = pl.add_mesh(pv.Sphere(), show_edges=True)
pl.show()
