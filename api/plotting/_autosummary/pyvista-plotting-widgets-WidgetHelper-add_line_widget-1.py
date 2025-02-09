# Shows an interactive line widget to move the sliced object like in `add_mesh_slice` function.
#
import pyvista as pv
from pyvista import examples
import numpy as np
model = examples.load_channels()
pl = pv.Plotter()
_ = pl.add_mesh(model, opacity=0.4)
def move_center(pointa, pointb):
    center = (np.array(pointa) + np.array(pointb)) / 2
    normal = np.array(pointa) - np.array(pointb)
    single_slc = model.slice(normal=normal, origin=center)

    _ = pl.add_mesh(single_slc, name='slc')
_ = pl.add_line_widget(callback=move_center, use_vertices=True)
pl.show()
