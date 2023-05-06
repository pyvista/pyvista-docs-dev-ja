# Slice the surface of a sphere.
#
import pyvista as pv
import vtk
sphere = vtk.vtkSphere()
sphere.SetRadius(10)
mesh = pv.Wavelet()
slice = mesh.slice_implicit(sphere)
slice.plot(show_edges=True, line_width=5)
#
sphere = vtk.vtkCylinder()
sphere.SetRadius(10)
mesh = pv.Wavelet()
slice = mesh.slice_implicit(sphere)
slice.plot(show_edges=True, line_width=5)
