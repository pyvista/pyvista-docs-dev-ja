# Add a custom observer.
#
import pyvista as pv
pl = pv.Plotter()
obs_enter = pl.iren.add_observer(
    "EnterEvent", lambda *_: print('Enter!')
)
