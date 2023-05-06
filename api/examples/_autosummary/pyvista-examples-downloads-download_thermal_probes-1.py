from pyvista import examples
dataset = examples.download_thermal_probes()
dataset.plot(
    render_points_as_spheres=True, point_size=5, cpos="xy"
)
