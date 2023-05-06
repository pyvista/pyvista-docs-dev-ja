from pyvista import examples
dataset = examples.download_horse_points()
dataset.plot(point_size=1)
