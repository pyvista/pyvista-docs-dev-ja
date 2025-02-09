import pyvista as pv
from pyvista import examples
#
mesh = pv.Sphere()
plotter = pv.Plotter()
actor = plotter.add_mesh(mesh)
actor = plotter.show_bounds(
    grid='front',
    location='outer',
    all_edges=True,
)
plotter.show()
#
# Control how many labels are displayed.
#
mesh = examples.load_random_hills()
#
plotter = pv.Plotter()
actor = plotter.add_mesh(mesh, cmap='terrain', show_scalar_bar=False)
actor = plotter.show_bounds(
    grid='back',
    location='outer',
    ticks='both',
    n_xlabels=2,
    n_ylabels=2,
    n_zlabels=2,
    xtitle='Easting',
    ytitle='Northing',
    ztitle='Elevation',
)
plotter.show()
#
# Hide labels, but still show axis titles.
#
plotter = pv.Plotter()
actor = plotter.add_mesh(mesh, cmap='terrain', show_scalar_bar=False)
actor = plotter.show_bounds(
    grid='back',
    location='outer',
    ticks='both',
    show_xlabels=False,
    show_ylabels=False,
    show_zlabels=False,
    xtitle='Easting',
    ytitle='Northing',
    ztitle='Elevation',
)
plotter.show()
