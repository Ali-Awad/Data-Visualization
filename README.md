# Data-Visualization

**Organize your images in a grid with quality values and color coding.**

Utilities for image grids with quality values and color coding. compare models side-by-side, show quality index (Q-index) or other metrics per sample, and build correlation layouts. Ideal for object detection, enhancement research, and organizing results.

## Quick Start

```bash
pip install -r requirements.txt
python demo.py
```

## Example Outputs

**Image grid with quality values and color coding** — Q-index or other metrics per sample:

![q-index](q-index.png)

## Structure

```
├── src/                  # Core utilities
│   ├── combine_img.py    # Image grid layout (combine_images, get_concat_h/v)
│   ├── generate_labels.py  # Text labels as PIL images
│   └── colorbar.py       # Custom colorbar as image
├── examples/             # Configurable example scripts
│   ├── violin_plot.py    # Violin plots from CSV
│   └── image_grid.py     # Model comparison grids
├── demo.py               # Demo (generates sample figures)
├── samples/              # Sample outputs
└── requirements.txt
```

## Requirements

- Python 3.8+
- matplotlib, numpy, pandas, Pillow, seaborn

Optional: `cmasher` for extended colormaps in `colbar()`.
