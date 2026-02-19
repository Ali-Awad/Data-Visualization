"""Custom colorbar generation for figures."""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from PIL import Image

try:
    import cmasher as cmr
    def _get_cmap(name, low, high):
        return cmr.get_sub_cmap(name, low, high)
except ImportError:
    def _get_cmap(name, low, high):
        base = mpl.cm.get_cmap(name)
        colors = base(np.linspace(low, high, 256))
        return mpl.colors.LinearSegmentedColormap.from_list("sub", colors)


def colbar(
    size=(800 * 4 + 40, 300),
    cmap_name="gist_rainbow",
    cmap_range=(0.03, 0.4),
    ticks=np.arange(0, 1.1, 0.1),
    labelcolor="#808080",
):
    """Generate a colorbar as a PIL Image.
    
    Args:
        size: (width, height) in pixels
        cmap_name: Matplotlib colormap name
        cmap_range: (low, high) fraction of colormap to use
        ticks: Tick positions
        labelcolor: Color for tick labels
    
    Returns:
        PIL Image of the colorbar
    """
    my_dpi = 92.60728755320785
    w, h = size
    
    plt.ioff()
    fig, ax = plt.subplots(figsize=(w / my_dpi, h / my_dpi), dpi=my_dpi)
    
    l, u = cmap_range
    cmap = _get_cmap(cmap_name, l, u)
    cbar = mpl.colorbar.ColorbarBase(
        ax, cmap=cmap, orientation="horizontal", ticks=ticks
    )
    cbar.ax.tick_params(
        labelsize=50, width=5, length=15,
        labelcolor=labelcolor, grid_color=labelcolor, color=labelcolor
    )
    plt.tight_layout(pad=1)
    fig.canvas.draw()
    buf = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    cols, rows = fig.canvas.get_width_height()
    buf = buf.reshape(rows, cols, 4)[:, :, :3].copy()
    x = Image.fromarray(buf)
    plt.close(fig)
    return x
