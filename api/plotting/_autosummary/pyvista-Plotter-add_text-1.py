# Add blue text to the upper right of the plotter.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_text(
    'Sample Text',
    position='upper_right',
    color='blue',
    shadow=True,
    font_size=26,
)
pl.show()
#
# Add text and use a custom freetype readable font file.
#
pl = pv.Plotter()
actor = pl.add_text(
    'Text',
    font_file='/home/user/Mplus2-Regular.ttf',
)  # doctest:+SKIP
