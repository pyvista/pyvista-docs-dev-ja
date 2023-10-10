import pyvista as pv
superquadric = pv.Superquadric(
    scale=(3.0, 1.0, 0.5),
    phi_roundness=0.1,
    theta_roundness=0.5,
)
superquadric.plot(show_edges=True)
