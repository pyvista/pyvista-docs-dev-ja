import pyvista as pv
from pyvista import examples
download_3ds_file = examples.download_3ds.download_iflamigm()
pl = pv.Plotter()
pl.import_3ds(download_3ds_file)
pl.show()
