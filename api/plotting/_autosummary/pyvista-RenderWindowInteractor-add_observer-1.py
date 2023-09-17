# Add a custom observer.
#
import pyvista
pl = pyvista.Plotter()
obs_enter = pl.iren.add_observer(
    "EnterEvent", lambda *_: print('Enter!')
)
