# Load data
#
import numpy as np
import pyvista as pv
from pyvista import examples
data = examples.load_frog_tissues()
#
# Plot tissue labels as a volume
#
# First, define plotting parameters
#
clim = data.get_data_range()  # Set color bar limits to match data
cmap = 'glasbey'  # Use a categorical colormap
categories = True  # Ensure n_colors matches number of labels
opacity = 'foreground'  # Make foreground opaque, background transparent
opacity_unit_distance = 1
#
# Set plotting resolution to half the image's spacing
#
res = np.array(data.spacing) / 2
#
# Define rendering parameters
#
mapper = 'gpu'
shade = True
ambient = 0.3
diffuse = 0.6
specular = 0.5
specular_power = 40
#
# Make and show plot
#
p = pv.Plotter()
_ = p.add_volume(
    data,
    clim=clim,
    ambient=ambient,
    shade=shade,
    diffuse=diffuse,
    specular=specular,
    specular_power=specular_power,
    mapper=mapper,
    opacity=opacity,
    opacity_unit_distance=opacity_unit_distance,
    categories=categories,
    cmap=cmap,
    resolution=res,
)
p.camera_position = 'yx'  # Set camera to provide a dorsal view
p.show()
#
# .. seealso::
#
#     :ref:`Frog Tissues Dataset <frog_tissues_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Frog Dataset <frog_dataset>`
#
#     :ref:`medical_dataset_gallery`
