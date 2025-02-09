from pyvista import examples
texture = examples.download_parched_canal_4k()
texture.dimensions
# Expected:
## (4096, 2048)
#
# Use :meth:`~pyvista.ImageDataFilters.resample` to downsample the texture's
# underlying image before plotting.
#
_ = texture.to_image().resample(0.25, inplace=True)
texture.dimensions
# Expected:
## (1024, 512)
#
texture.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Parched Canal 4k Dataset <parched_canal_4k_dataset>`
