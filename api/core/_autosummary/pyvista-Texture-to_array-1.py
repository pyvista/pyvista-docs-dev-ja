from pyvista import examples
texture = examples.download_puppy_texture()
texture  # doctest:+SKIP
# Expected:
## Texture (...)
##   Components:   3
##   Cube Map:     False
##   Dimensions:   1600, 1200
texture.to_array().shape
# Expected:
## (1200, 1600, 3)
texture.to_array().dtype
# Expected:
## dtype('uint8')
