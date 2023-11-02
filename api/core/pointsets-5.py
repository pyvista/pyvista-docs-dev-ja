# Animate plot as a wire-frame
plotter = pv.Plotter(window_size=(800, 600))
plotter.add_mesh(grid, scalars='Y Displacement',
                 show_edges=True,
                 rng=[-d.max(), d.max()], interpolate_before_map=True,
                 style='wireframe')
plotter.add_axes()
plotter.camera_position = cpos

plotter.open_gif('beam_wireframe.gif')
for phase in np.linspace(0, 2*np.pi, 20):
    grid.points = pts + d * np.cos(phase)
    grid['Y Displacement'] = d[:, 1] * np.cos(phase)
    plotter.write_frame()

# close the plotter when complete
plotter.close()