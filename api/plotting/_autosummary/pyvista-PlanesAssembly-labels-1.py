import pyvista as pv
planes = pv.PlanesAssembly()
planes.labels = ['Sagittal', 'Coronal', 'Transverse']
planes.labels
# Expected:
## ('Sagittal', 'Coronal', 'Transverse')
