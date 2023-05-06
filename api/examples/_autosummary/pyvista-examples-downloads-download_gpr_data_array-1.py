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
