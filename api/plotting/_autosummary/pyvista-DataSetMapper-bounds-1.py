import pyvista as pv
mapper = pv.DataSetMapper(dataset=pv.Cube())
mapper.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=0.5, y_min=-0.5, y_max=0.5, z_min=-0.5, z_max=0.5)
