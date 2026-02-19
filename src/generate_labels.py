"""Generate text labels as images for figure annotations."""

from PIL import Image, ImageDraw, ImageFont
import os


def _get_font(size=75):
    """Try common font paths; fall back to default."""
    fonts = [
        "Arial.ttf",
        "arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for name in fonts:
        try:
            return ImageFont.truetype(name, size=size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def generate_label(
    labels,
    label_size=(800, 200),
    fontSize=75,
    offset=0,
    rotation=0,
    line=False,
    color="#808080",
    background="white",
):
    """Create image(s) with centered text labels.
    
    Args:
        labels: List of text strings
        label_size: (width, height) for each label
        fontSize: Font size
        offset: Vertical text offset
        rotation: Rotation in degrees
        line: Draw line above text
        color: Text color (hex)
        background: Background fill for text box (None to disable)
    
    Returns:
        List of PIL Images
    """
    font = _get_font(fontSize)
    images = []
    
    for label in labels:
        width, height = label_size
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)
        
        _, _, textWidth, textHeight = draw.textbbox((0, 0), label, font=font)
        xText = (width - textWidth) / 2
        yText = ((height - textHeight) / 2) + offset
        
        if background:
            left, top, right, bottom = draw.textbbox((xText, yText), label, font=font)
            draw.rectangle((left - 50, top - 10, right + 50, bottom + 10), fill=background)
        draw.text((xText, yText), label, font=font, fill=color, stroke_width=1, stroke_fill="black")
        
        if line:
            draw.line((xText, yText - 30, xText + textWidth, yText - 30), fill=color, width=50)
        
        if rotation:
            img = img.rotate(rotation, expand=True)
        images.append(img)
    
    return images
