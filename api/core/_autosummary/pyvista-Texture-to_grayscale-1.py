from pyvista import examples
texture = examples.download_masonry_texture()
bw_texture = texture.to_grayscale()
bw_texture
# Expected:
## Texture (...)
##   Components:   1
##   Cube Map:     False
##   Dimensions:   256, 256
bw_texture.plot()
