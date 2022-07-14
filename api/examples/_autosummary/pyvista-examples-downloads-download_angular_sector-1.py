from pyvista import examples
dataset = examples.download_angular_sector()
dataset.plot(scalars='PointId')
