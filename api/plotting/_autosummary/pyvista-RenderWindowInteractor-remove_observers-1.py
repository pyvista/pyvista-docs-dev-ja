# Add two observers and immediately remove them.
#
import pyvista as pv
pl = pv.Plotter()
obs_enter = pl.iren.add_observer(
    "EnterEvent", lambda *_: print('Enter!')
)
obs_leave = pl.iren.add_observer(
    "LeaveEvent", lambda *_: print('Leave!')
)
pl.iren.remove_observers()
