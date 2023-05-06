import pyvista
mesh = pyvista.Sphere()
mesh.get_cell(0).points
# Expected:
## array([[-5.40595092e-02,  0.00000000e+00, -4.97068971e-01],
##        [-5.28781787e-02,  1.12396041e-02, -4.97068971e-01],
##        [-5.55111512e-17,  0.00000000e+00, -5.00000000e-01]])
