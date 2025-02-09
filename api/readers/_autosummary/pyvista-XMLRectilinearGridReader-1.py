import pyvista as pv
from pyvista import examples
filename = examples.download_rectilinear_grid(load=False)
filename.split('/')[-1]  # omit the path
# Expected:
## 'RectilinearGrid.vtr'
reader = pv.get_reader(filename)
mesh = reader.read()
sliced_mesh = mesh.slice('y')
sliced_mesh.plot(
    scalars='Void Volume Fraction',
    cpos='xz',
    show_scalar_bar=False,
)
