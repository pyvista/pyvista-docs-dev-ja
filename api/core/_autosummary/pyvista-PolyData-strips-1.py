import pyvista as pv
polygon = pv.Rectangle()
extruded = polygon.extrude((0, 0, 1), capping=False)
extruded.strips
# Expected:
## array([4, 0, 1, 4, 5, 4, 1, 2, 5, 6, 4, 2, 3, 6, 7, 4, 3, 0, 7, 4])
