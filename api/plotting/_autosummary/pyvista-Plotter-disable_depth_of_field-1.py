import pyvista as pv
pl = pv.Plotter(lighting='three lights')
pl.enable_depth_of_field()
pl.disable_depth_of_field()
