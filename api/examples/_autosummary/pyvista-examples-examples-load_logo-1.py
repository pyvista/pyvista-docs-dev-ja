from pyvista import examples
image = examples.load_logo()
image.dimensions
# Expected:
## (1389, 592, 1)
#
image.plot(cpos='xy', zoom='tight', rgb=True, show_axes=False)
#
# .. seealso::
#
#     :ref:`Logo Dataset <logo_dataset>`
