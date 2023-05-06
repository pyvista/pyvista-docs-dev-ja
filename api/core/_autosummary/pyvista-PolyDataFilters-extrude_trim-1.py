# Extrude a disc.
#
import pyvista
import numpy as np
plane = pyvista.Plane(
    i_size=2, j_size=2, direction=[0, 0.8, 1]
)
disc = pyvista.Disc(center=(0, 0, -1), c_res=50)
direction = [0, 0, 1]
extruded_disc = disc.extrude_trim(direction, plane)
extruded_disc.plot(smooth_shading=True, split_sharp_edges=True)
