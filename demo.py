#!/usr/bin/env python3
"""
Demo script generating two sample figures using the visualization utilities.
Run: python demo.py
Outputs: samples/correlation_grid.jpeg, samples/image_grid.jpeg
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

from src import combine_images, get_concat_h, generate_label, colbar
from PIL import Image, ImageOps

OUT_DIR = "samples"
os.makedirs(OUT_DIR, exist_ok=True)


def create_dummy_plots(n=8, w=400, h=300):
    """Create n dummy regression/scatter plot images for demo."""
    np.random.seed(42)
    images = []
    metrics = ["UIQM", "UCIQE", "CCF", "Entropy"] * 2  # 8 for 2 datasets
    for m in metrics[:n]:
        fig, ax = plt.subplots(figsize=(w / 100, h / 100), dpi=100)
        x = np.random.randn(50) * 0.3
        y = x + np.random.randn(50) * 0.2
        ax.scatter(x, y, alpha=0.6, s=30)
        ax.set_xlabel(f"Δ {m}", fontsize=9)
        ax.set_ylabel("Δ Q-index", fontsize=9)
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.axhline(0, color="gray", ls="--", alpha=0.5)
        ax.axvline(0, color="gray", ls="--", alpha=0.5)
        plt.tight_layout()
        fig.canvas.draw()
        buf = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
        cols, rows = fig.canvas.get_width_height()
        buf = buf.reshape(rows, cols, 4)[:, :, :3]
        images.append(Image.fromarray(buf))
        plt.close(fig)
    return images


def create_dummy_images(n=6, size=200):
    """Create n×n dummy colored squares as placeholder images."""
    rng = np.random.default_rng(42)
    imgs = []
    for _ in range(n):
        arr = (rng.random((size, size, 3)) * 200 + 55).astype(np.uint8)
        imgs.append(Image.fromarray(arr))
    return imgs


def figure1_correlation_grid():
    """Figure 1: Detection–Enhancement correlation grid (like generate_figure.py)."""
    print("Generating Figure 1: Correlation grid...")
    plots = create_dummy_plots(n=8, w=400, h=300)
    
    dataset_labels = generate_label(
        ["CUPDD", "RUOD"], label_size=(300, 80), fontSize=36, rotation=90
    )
    layer1 = combine_images(columns=1, space=0, images=dataset_labels)
    layer2 = combine_images(columns=4, space=0, images=plots)
    figure = combine_images(columns=2, space=0, images=[layer1, layer2])
    
    cbar_img = colbar(size=(figure.size[0], 120))
    pad = generate_label([""], label_size=(100, 75), fontSize=30)[0]
    legend_row = get_concat_h(pad, cbar_img)
    legend_row = get_concat_h(legend_row, pad)
    legend_row = ImageOps.expand(legend_row, border=10, fill="gray")
    
    figure = combine_images(columns=1, space=0, images=[figure, legend_row])
    arr = np.asarray(figure)
    path = os.path.join(OUT_DIR, "correlation_grid.jpeg")
    plt.imsave(path, arr, cmap=None, format="jpeg")
    print(f"  Saved: {path}")


def figure2_image_grid():
    """Figure 2: Model comparison image grid (like species grids)."""
    print("Generating Figure 2: Image grid...")
    models = ["Original", "Model A", "Model B"]
    n_samples = 3
    dummy_imgs = create_dummy_images(n=len(models) * n_samples, size=180)
    
    title = []
    for m in models:
        title.append(generate_label([m], label_size=(200, 80), fontSize=50)[0])
    titles = combine_images(columns=len(title), space=10, images=title)
    
    filler = generate_label([""], label_size=(80, 80), fontSize=30)[0]
    full_title = combine_images(columns=2, space=10, images=[filler, titles])
    
    images = []
    for i in range(n_samples):
        images.append(
            generate_label([f"Sample #{i+1}"], label_size=(180, 80), fontSize=40, rotation=90)[0]
        )
        for j, m in enumerate(models):
            idx = i * len(models) + j
            images.append(dummy_imgs[idx])
    
    grid = combine_images(columns=len(models) + 1, space=10, images=images)
    figure = combine_images(columns=1, space=20, images=[full_title, grid])
    arr = np.asarray(figure)
    path = os.path.join(OUT_DIR, "image_grid.jpeg")
    plt.imsave(path, arr, cmap=None, format="jpeg")
    print(f"  Saved: {path}")


def main():
    figure1_correlation_grid()
    figure2_image_grid()
    print("\nDone. Sample outputs in ./samples/")


if __name__ == "__main__":
    main()
