import pyvista as pv
planes = pv.PlanesAssembly()
planes.y_label = 'This plane'
planes.y_label
# Expected:
## 'This plane'
