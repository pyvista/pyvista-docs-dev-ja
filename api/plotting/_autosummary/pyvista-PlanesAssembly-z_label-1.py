import pyvista as pv
planes = pv.PlanesAssembly()
planes.z_label = 'This plane'
planes.z_label
# Expected:
## 'This plane'
