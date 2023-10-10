import pyvista as pv
from pyvista import examples
dataset = examples.download_head_2()
pl = pv.Plotter()
_ = pl.add_volume(dataset, cmap="cool", opacity="sigmoid_6")
pl.show()
