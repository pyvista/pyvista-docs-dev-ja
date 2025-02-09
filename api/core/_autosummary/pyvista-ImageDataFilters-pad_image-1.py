# Pad a grayscale image with a 100-pixel wide border. The padding is black
# (i.e. has a value of ``0``) by default.
#
import pyvista as pv
from pyvista import examples
gray_image = examples.download_moonlanding_image()
gray_image.dimensions
# Expected:
## (630, 474, 1)
padded = gray_image.pad_image(pad_size=100)
padded.dimensions
# Expected:
## (830, 674, 1)
#
# Plot the image. To show grayscale images correctly, we define a custom plotting
# method.
#
def grayscale_image_plotter(image):
    import vtk

    actor = vtk.vtkImageActor()
    actor.GetMapper().SetInputData(image)
    actor.GetProperty().SetInterpolationTypeToNearest()
    plot = pv.Plotter()
    plot.add_actor(actor)
    plot.view_xy()
    plot.camera.tight()
    return plot
plot = grayscale_image_plotter(padded)
plot.show()
#
# Pad only the x-axis with a white border.
#
padded = gray_image.pad_image(pad_value=255, pad_size=(200, 0))
plot = grayscale_image_plotter(padded)
plot.show()
#
# Pad with wrapping.
#
padded = gray_image.pad_image('wrap', pad_size=100)
plot = grayscale_image_plotter(padded)
plot.show()
#
# Pad with mirroring.
#
padded = gray_image.pad_image('mirror', pad_size=100)
plot = grayscale_image_plotter(padded)
plot.show()
#
# Pad a color image using multi-component color vectors. Here, RGBA values are
# used.
#
color_image = examples.download_beach()
red = (255, 0, 0)  # RGB
padded = color_image.pad_image(pad_value=red, pad_size=50)
plot_kwargs = dict(cpos='xy', zoom='tight', rgb=True, show_axes=False)
padded.plot(**plot_kwargs)
#
# Pad each edge of the image separately with a different color.
#
orange = pv.Color('orange').int_rgb
purple = pv.Color('purple').int_rgb
blue = pv.Color('blue').int_rgb
green = pv.Color('green').int_rgb
padded = color_image.pad_image(orange, pad_size=(25, 0, 0, 0))
padded = padded.pad_image(purple, pad_size=(0, 25, 0, 0))
padded = padded.pad_image(blue, pad_size=(0, 0, 25, 0))
padded = padded.pad_image(green, pad_size=(0, 0, 0, 25))
padded.plot(**plot_kwargs)
