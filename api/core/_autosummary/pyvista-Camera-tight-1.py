# Display the puppy image with a tight view.
#
import pyvista as pv
from pyvista import examples
puppy = examples.download_puppy()
pl = pv.Plotter(border=True, border_width=5)
_ = pl.add_mesh(puppy, rgb=True)
pl.camera.tight()
pl.show()
#
# Set the background to blue use a 5% padding around the image.
#
pl = pv.Plotter()
_ = pl.add_mesh(puppy, rgb=True)
pl.background_color = 'b'
pl.camera.tight(padding=0.05)
pl.show()
