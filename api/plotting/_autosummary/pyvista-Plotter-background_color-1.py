# Set the background color to ``"pink"`` and plot it.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube(), show_edges=True)
pl.background_color = 'pink'
pl.background_color
# Expected:
## Color(name='pink', hex='#ffc0cbff', opacity=255)
pl.show()
