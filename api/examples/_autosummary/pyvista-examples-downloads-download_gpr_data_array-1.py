from pyvista import examples
dataset = examples.download_gpr_data_array()  # doctest:+SKIP
dataset  # doctest:+SKIP
# Expected:
## array([[nan, nan, nan, ..., nan, nan, nan],
##        [nan, nan, nan, ..., nan, nan, nan],
##        [nan, nan, nan, ..., nan, nan, nan],
##        ...,
##        [ 0.,  0.,  0., ...,  0.,  0.,  0.],
##        [ 0.,  0.,  0., ...,  0.,  0.,  0.],
##        [ 0.,  0.,  0., ...,  0.,  0.,  0.]])
#
# .. seealso::
#
#     :ref:`Gpr Data Array Dataset <gpr_data_array_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Gpr Path Dataset <gpr_path_dataset>`
#
#     :ref:`create_draped_surf_example`
