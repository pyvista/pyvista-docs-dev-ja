# Use an north arrow as the orientation widget.
#
import pyvista as pv
from pyvista import examples
terrain = examples.download_st_helens().warp_by_scalar()
pl = pv.Plotter()
actor = pl.add_mesh(terrain)
widget = pl.add_north_arrow_widget()
pl.enable_terrain_style(True)
pl.show()
