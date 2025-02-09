# Fit planes to a model of a human.
#
import numpy as np
import pyvista as pv
from pyvista import examples
human = examples.download_human()
labels = 'Sagittal', 'Coronal', 'Transverse'
planes = pv.PlanesAssembly(
    bounds=human.bounds, labels=labels, label_size=25
)
#
# Plot the planes and the model.
#
pl = pv.Plotter()
human_actor = pl.add_mesh(human, scalars='Color', rgb=True)
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
#
# Apply a transformation to the planes and the model.
#
transform = np.array(
    [
        [0.70645893, 0.69636424, 0.12646197, 1.0],
        [-0.62246712, 0.69636424, -0.35722756, 2.0],
        [-0.33682409, 0.17364818, 0.92541658, 3.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
)
planes.user_matrix = transform
human_actor.user_matrix = transform
#
pl = pv.Plotter()
_ = pl.add_actor(human_actor)
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
#
# Create a new assembly and customize the colors and opacity.
#
color = pv.global_theme.color
planes = pv.PlanesAssembly(
    bounds=human.bounds,
    x_color=color,
    y_color=color,
    z_color=color,
    opacity=1.0,
)
#
# Since the planes are opaque, the 3D labels may be occluded. Use 2D labels instead
# so the labels are always visible.
#
planes.label_mode = '2D'
#
# Offset the labels to position them inside the bounds of the planes.
#
planes.label_offset = -0.05
#
# Move the labels for the two larger planes closer to the corners.
#
planes.label_position = (0.8, 0.8, 0.5)
#
# Visualize the result.
#
pl = pv.Plotter()
_ = pl.add_mesh(human, scalars='Color', rgb=True)
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
