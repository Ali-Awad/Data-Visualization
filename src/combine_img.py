"""Image grid combiner for side-by-side layouts."""

from PIL import Image
import math


def combine_images(columns, space, images):
    """Arrange images in a grid layout.
    
    Args:
        columns: Number of images per row
        space: Pixel spacing between images
        images: List of PIL Images
    
    Returns:
        Combined PIL Image (RGBA)
    """
    rows = len(images) // columns
    if len(images) % columns:
        rows += 1
    width_sum = sum(img.size[0] for img in images)
    height_sum = sum(img.size[1] for img in images)
    background_width = width_sum // rows + (space * columns) - space
    background_height = height_sum // columns + (space * rows) - space
    background = Image.new("RGBA", (background_width, background_height), (255, 255, 255, 255))
    
    x, y = 0, 0
    for i, img in enumerate(images):
        background.paste(img, (x, y))
        x += img.width + space
        if (i + 1) % columns == 0:
            y += img.height + space
            x = 0
    return background


def get_concat_h(im1, im2):
    """Concatenate two images horizontally."""
    dst = Image.new("RGB", (im1.width + im2.width, im1.height), (255, 255, 255, 255))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def get_concat_v(im1, im2, space=0):
    """Concatenate two images vertically, centered."""
    w1, h1 = im1.size
    w2, h2 = im2.size
    dst = Image.new("RGB", (max(w1, w2), h1 + space + h2), (255, 255, 255, 255))
    dst.paste(im1, (abs(math.floor((w2 - w1) / 2)), 0))
    dst.paste(im2, (0, space + h1))
    return dst
