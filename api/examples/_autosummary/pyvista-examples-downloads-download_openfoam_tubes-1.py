# Plot the outline of the dataset along with a cross section of the flow velocity.
#
import pyvista as pv
from pyvista import examples
dataset = examples.download_openfoam_tubes()
air = dataset[0]
y_slice = air.slice('y')
pl = pv.Plotter()
_ = pl.add_mesh(
    y_slice,
    scalars='U',
    lighting=False,
    scalar_bar_args={'title': 'Flow Velocity'},
)
_ = pl.add_mesh(air, color='w', opacity=0.25)
pl.enable_anti_aliasing()
pl.show()
