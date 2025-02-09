# Generate a binary mask from a coarse mesh.
#
import numpy as np
import pyvista as pv
from pyvista import examples
poly = examples.download_bunny_coarse()
mask = poly.voxelize_binary_mask()
#
# The mask is stored as :class:`~pyvista.ImageData` with point data scalars
# (zeros for background, ones for foreground).
#
mask
# Expected:
## ImageData (...)
##   N Cells:      7056
##   N Points:     8228
##   X Bounds:     -1.245e-01, 1.731e-01
##   Y Bounds:     -1.135e-01, 1.807e-01
##   Z Bounds:     -1.359e-01, 9.140e-02
##   Dimensions:   22, 22, 17
##   Spacing:      1.417e-02, 1.401e-02, 1.421e-02
##   N Arrays:     1
#
np.unique(mask.point_data['mask'])
# Expected:
## pyvista_ndarray([0, 1], dtype=uint8)
#
# To visualize it as voxel cells, use :meth:`~pyvista.ImageDataFilters.points_to_cells`,
# then use :meth:`~pyvista.DataSetFilters.threshold` to extract the foreground.
#
# We also plot the voxel cells in blue and the input poly data in green for
# comparison.
#
def mask_and_polydata_plotter(mask, poly):
    voxel_cells = mask.points_to_cells().threshold(0.5)

    plot = pv.Plotter()
    _ = plot.add_mesh(voxel_cells, color='blue')
    _ = plot.add_mesh(poly, color='lime')
    plot.camera_position = 'xy'
    return plot
#
plot = mask_and_polydata_plotter(mask, poly)
plot.show()
#
# The spacing of the mask image is automatically adjusted to match the
# density of the input.
#
# Repeat the previous example with a finer mesh.
#
poly = examples.download_bunny()
mask = poly.voxelize_binary_mask()
plot = mask_and_polydata_plotter(mask, poly)
plot.show()
#
# Control the spacing manually instead. Here, a very coarse spacing is used.
#
mask = poly.voxelize_binary_mask(spacing=(0.01, 0.04, 0.02))
plot = mask_and_polydata_plotter(mask, poly)
plot.show()
#
# Note that the spacing is only approximate. Check the mask's actual spacing.
#
mask.spacing
# Expected:
## (0.009731187485158443, 0.03858340159058571, 0.020112216472625732)
#
# The actual values may be greater or less than the specified values. Use
# ``rounding_func=np.floor`` to force all values to be greater.
#
mask = poly.voxelize_binary_mask(
    spacing=(0.01, 0.04, 0.02), rounding_func=np.floor
)
mask.spacing
# Expected:
## (0.01037993331750234, 0.05144453545411428, 0.020112216472625732)
#
# Set the dimensions instead of the spacing.
#
mask = poly.voxelize_binary_mask(dimensions=(10, 20, 30))
plot = mask_and_polydata_plotter(mask, poly)
plot.show()
#
mask.dimensions
# Expected:
## (10, 20, 30)
#
# Create a mask using a reference volume. First generate polydata from
# an existing mask.
#
volume = examples.load_frog_tissues()
poly = volume.contour_labels()
#
# Now create the mask from the polydata using the volume as a reference.
#
mask = poly.voxelize_binary_mask(reference_volume=volume)
plot = mask_and_polydata_plotter(mask, poly)
plot.show()
#
# Visualize the effect of internal surfaces.
#
mesh = pv.Cylinder() + pv.Cylinder((0, 0.75, 0))
binary_mask = mesh.voxelize_binary_mask(
    dimensions=(1, 100, 50)
).points_to_cells()
plot = pv.Plotter()
_ = plot.add_mesh(binary_mask)
_ = plot.add_mesh(mesh.slice(), color='red')
plot.show(cpos='yz')
#
# Note how the intersection is excluded from the mask.
# To include the voxels delimited by internal surfaces in the foreground, the internal
# surfaces should be removed, for instance by applying a boolean union. Note that
# this operation in unreliable in VTK but may be performed with external tools such
# as `vtkbool <https://github.com/zippy84/vtkbool>`_.
#
# Alternatively, the intersecting parts of the mesh can be processed sequentially.
#
cylinder_1 = pv.Cylinder()
cylinder_2 = pv.Cylinder((0, 0.75, 0))
#
reference_volume = pv.ImageData(
    dimensions=(1, 100, 50),
    spacing=(1, 0.0175, 0.02),
    origin=(0, -0.5 + 0.0175 / 2, -0.5 + 0.02 / 2),
)
#
binary_mask_1 = cylinder_1.voxelize_binary_mask(
    reference_volume=reference_volume
).points_to_cells()
binary_mask_2 = cylinder_2.voxelize_binary_mask(
    reference_volume=reference_volume
).points_to_cells()
#
binary_mask_1['mask'] = binary_mask_1['mask'] | binary_mask_2['mask']
#
plot = pv.Plotter()
_ = plot.add_mesh(binary_mask_1)
_ = plot.add_mesh(cylinder_1.slice(), color='red')
_ = plot.add_mesh(cylinder_2.slice(), color='red')
plot.show(cpos='yz')
#
# When multiple internal surfaces are nested, they are successively treated as
# interfaces between background and foreground.
#
mesh = pv.Tube(radius=2) + pv.Tube(radius=3) + pv.Tube(radius=4)
binary_mask = mesh.voxelize_binary_mask(
    dimensions=(1, 50, 50)
).points_to_cells()
plot = pv.Plotter()
_ = plot.add_mesh(binary_mask)
_ = plot.add_mesh(mesh.slice(), color='red')
plot.show(cpos='yz')
