from PIL import Image, ImageDraw, ImageFont
import textwrap
def generateImage(text,image_width,image_height):
    img = Image.new('RGB', (image_width, image_height), color = 'white')
    
    #Changing the font type and re-scaling the text size
    font_size=1
    font = ImageFont.truetype("arial.ttf",font_size)
    width, height = font.getsize('0'*40)
    while(width<image_width):
        font_size=font_size+1
        font = ImageFont.truetype("arial.ttf",font_size)
        width, height = font.getsize('0'*40)

    #font_size=font_size-1
    #font = ImageFont.truetype("arial.ttf",font_size)

    #Customizing an image
    d = ImageDraw.Draw(img)
    #w, h = font.getsize(text)
    
    lines = textwrap.wrap(text, width=40)
    y_text = 0
    for line in lines:
        width, height = font.getsize(line)
        d.text((0, y_text), line, font = font, fill=(175,175,175))
        y_text += height

    
    
    return img
