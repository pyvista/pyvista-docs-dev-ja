# Load a texture from file. File should be a "image" or "image-like" file.
#
import os
import pyvista as pv
from pyvista import examples
path = examples.download_masonry_texture(load=False)
os.path.basename(path)
# Expected:
## 'masonry.bmp'
texture = pv.Texture(path)
texture
# Expected:
## Texture (...)
##   Components:   3
##   Cube Map:     False
##   Dimensions:   256, 256
#
# Create a texture from an RGB array. Note how this is colored per "point"
# rather than per "pixel".
#
import numpy as np
arr = np.array(
    [
        [255, 255, 255],
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
    ],
    dtype=np.uint8,
)
arr = arr.reshape((2, 2, 3))
texture = pv.Texture(arr)
texture.plot()
#
# Create a cubemap from 6 images.
#
px = examples.download_sky(direction='posx')  # doctest:+SKIP
nx = examples.download_sky(direction='negx')  # doctest:+SKIP
py = examples.download_sky(direction='posy')  # doctest:+SKIP
ny = examples.download_sky(direction='negy')  # doctest:+SKIP
pz = examples.download_sky(direction='posz')  # doctest:+SKIP
nz = examples.download_sky(direction='negz')  # doctest:+SKIP
texture = pv.Texture([px, nx, py, ny, pz, nz])  # doctest:+SKIP
texture.cube_map  # doctest:+SKIP
# Expected:
## True
