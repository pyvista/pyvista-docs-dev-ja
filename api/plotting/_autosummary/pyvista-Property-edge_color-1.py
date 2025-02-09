# Get the default edge color and visualize it. Set the edge's visibility
# to ``True`` so we can see them.
#
import pyvista as pv
prop = pv.Property()
prop.edge_color
# Expected:
## Color(name='black', hex='#000000ff', opacity=255)
#
prop.show_edges = True
prop.plot()
#
# Visualize red edges.
#
prop.edge_color = 'red'
prop.plot()
