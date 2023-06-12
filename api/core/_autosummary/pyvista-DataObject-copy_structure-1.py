import pyvista as pv
source = pv.ImageData(dimensions=(10, 10, 5))
target = pv.ImageData()
target.copy_structure(source)
target.plot(show_edges=True)
