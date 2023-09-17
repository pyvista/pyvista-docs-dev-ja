# Add an observer and immediately remove it.
#
import pyvista
pl = pyvista.Plotter()
obs_enter = pl.iren.add_observer(
    "EnterEvent", lambda *_: print('Enter!')
)
pl.iren.remove_observer(obs_enter)
