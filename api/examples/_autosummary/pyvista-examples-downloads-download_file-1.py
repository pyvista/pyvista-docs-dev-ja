# Download the ``'puppy.jpg'`` image.
#
from pyvista import examples
path = examples.download_file('puppy.jpg')  # doctest:+SKIP
path  # doctest:+SKIP
# Expected:
## '/home/user/.cache/pyvista_3/puppy.jpg'
