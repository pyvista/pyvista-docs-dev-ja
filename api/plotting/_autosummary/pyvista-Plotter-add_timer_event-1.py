# Add a timer to a Plotter to move a sphere across a scene.
#
import pyvista as pv
sphere = pv.Sphere()
pl = pv.Plotter()
actor = pl.add_mesh(sphere)
def callback(step):
    actor.position = [step / 100.0, step / 100.0, 0]
pl.add_timer_event(
    max_steps=200, duration=500, callback=callback
)
