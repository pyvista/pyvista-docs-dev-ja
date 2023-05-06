# Apply FFT to an example image.
#
from pyvista import examples
image = examples.download_moonlanding_image()
fft_image = image.fft()
fft_image.point_data  # doctest:+SKIP
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : PNGImage
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
## PNGImage                complex128 (298620,)          SCALARS
