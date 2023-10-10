import pyvista as pv
from pyvista import examples
dataset = examples.download_head()
pl = pv.Plotter()
_ = pl.add_volume(dataset, cmap="cool", opacity="sigmoid_6")
pl.camera_position = [
    (-228.0, -418.0, -158.0),
    (94.0, 122.0, 82.0),
    (-0.2, -0.3, 0.9),
]
pl.show()
#
# See :ref:`volume_rendering_example` for an example using this
