#!/usr/bin/env python3
"""
Example: Build an image grid comparing models/samples.
Layout: rows = samples, columns = models (with row labels).

Usage:
  python examples/image_grid.py --root-dir ./images --models Original,ModelA,ModelB --samples s1,s2,s3 --out grid.jpeg
"""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import combine_images, generate_label
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def main():
    p = argparse.ArgumentParser(description="Create model comparison image grid")
    p.add_argument("--root-dir", required=True, help="Root dir with {model}/{sample}.png")
    p.add_argument("--models", required=True, help="Comma-separated model names")
    p.add_argument("--samples", required=True, help="Comma-separated sample IDs")
    p.add_argument("--ext", default="png")
    p.add_argument("--out", default="grid.jpeg")
    args = p.parse_args()

    root = Path(args.root_dir)
    models = [m.strip() for m in args.models.split(",")]
    samples = [s.strip() for s in args.samples.split(",")]

    titles = [generate_label([m], label_size=(300, 80), fontSize=50)[0] for m in models]
    row_titles = combine_images(columns=len(titles), space=10, images=titles)
    filler = generate_label([""], label_size=(80, 80), fontSize=30)[0]
    full_title = combine_images(columns=2, space=10, images=[filler, row_titles])

    images = []
    for sample in samples:
        images.append(generate_label([sample], label_size=(200, 80), fontSize=40, rotation=90)[0])
        for model in models:
            path = root / model / f"{sample}.{args.ext}"
            if path.exists():
                images.append(Image.open(path))
            else:
                images.append(Image.new("RGB", (200, 200), color=(200, 200, 200)))

    grid = combine_images(columns=len(models) + 1, space=10, images=images)
    figure = combine_images(columns=1, space=20, images=[full_title, grid])
    arr = np.asarray(figure)
    plt.imsave(args.out, arr, cmap=None, format="jpeg")
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
