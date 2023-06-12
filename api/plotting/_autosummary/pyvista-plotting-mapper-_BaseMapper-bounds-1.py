import pyvista as pv
mapper = pv.DataSetMapper(dataset=pv.Cube())
mapper.bounds
# Expected:
## (-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
