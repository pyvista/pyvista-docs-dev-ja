# Return the points of a Sphere as a :class:`pyvista.pyvista_ndarray`.
#
import pyvista as pv
mesh = pv.Sphere()
mesh.points  # doctest:+SKIP
# Expected:
## pyvista_ndarray([[-5.5511151e-17,  0.0000000e+00, -5.0000000e-01],
##                  [ 5.5511151e-17,  0.0000000e+00,  5.0000000e-01],
##                  [-5.4059509e-02,  0.0000000e+00, -4.9706897e-01],
##                  ...,
##                  [-1.5616201e-01, -3.3193260e-02,  4.7382659e-01],
##                  [-1.0513641e-01, -2.2347433e-02,  4.8831028e-01],
##                  [-5.2878179e-02, -1.1239604e-02,  4.9706897e-01]],
##                 dtype=float32)
