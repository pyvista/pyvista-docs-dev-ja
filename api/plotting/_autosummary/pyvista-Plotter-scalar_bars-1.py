import pyvista as pv
sphere = pv.Sphere()
sphere['Data'] = sphere.points[:, 2]
plotter = pv.Plotter()
_ = plotter.add_mesh(sphere)
plotter.scalar_bars
# Expected:
## Scalar Bar Title     Interactive
## "Data"               False
#
# Select a scalar bar actor based on the title of the bar.
#
plotter.scalar_bars['Data']
# Expected:
## <vtkmodules.vtkRenderingAnnotation.vtkScalarBarActor(...) at ...>
