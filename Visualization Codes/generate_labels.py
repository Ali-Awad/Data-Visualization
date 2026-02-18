from PIL import Image, ImageDraw, ImageFont

def generate_label(labels, label_size = (800, 200), fontSize = 75, offset = 0, rotation = 0, line = False, color='#808080', background= "white"):
    images = []
    for label in labels:
        print(label)
        width, height = label_size
    
        font = ImageFont.truetype("arial.ttf", size=fontSize)
        img = Image.new('RGB', (width, height), color='white')
        
        imgDraw = ImageDraw.Draw(img)
        
        _, _, textWidth, textHeight = imgDraw.textbbox((0, 0),label, font=font)
        xText = (width - textWidth) / 2
        yText = ((height - textHeight) / 2) + offset #to shift the text up and down
        
        if background:
            left, top, right, bottom = imgDraw.textbbox((xText, yText), label, font=font)
            imgDraw.rectangle((left-50, top-10, right+50, bottom+10), fill=background)
        imgDraw.text((xText, yText), label, font=font, fill=color, stroke_width=1, stroke_fill='black')#(0, 0, 0))
        if line:
            imgDraw.line((xText,yText-30, xText+textWidth, yText-30), fill=color, width=50)#line above
            #imgDraw.line((xText,height, xText+textWidth, height), fill=color, width=10) #line below
        #img.convert("RGBA")
        img = img.rotate(rotation, expand=True)
        images.append(img)
    return images