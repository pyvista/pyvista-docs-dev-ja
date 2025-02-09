import pyvista as pv
pl = pv.Plotter()
pl.camera.to_paraview_pvcc('camera.pvcc')  # doctest:+SKIP
