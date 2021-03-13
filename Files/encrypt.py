from PIL import Image,ImageDraw
import PIL
from tkinter.filedialog import asksaveasfilename 

def processInts(n1,n2):
    n1_as_string=str(n1)
    n1_as_string='0'*(3-len(n1_as_string))+n1_as_string
    n2_as_string=str(n2)
    n2_as_string='0'*(3-len(n2_as_string))+n2_as_string
    avg=int((int(n1_as_string[1])+int(n2_as_string[1]))/2)
    final_value=int(n1_as_string[0]+str(avg)+n2_as_string[0])
    return final_value



def clubPixels(pixel1,pixel2):

    pixel_n=(processInts(pixel1[0],pixel2[0]),processInts(pixel1[1],pixel2[1]),processInts(pixel1[2],pixel2[2]))
    return pixel_n


def encryptImage(base_image,hidden_image):
    
    width,height=base_image.size
    encrypted_image = Image.new('RGB', (width,height), color = 'red')
    for x in range(width):
        for y in range(height):
            target_pixel=clubPixels(base_image.getpixel((x,y)),hidden_image.getpixel((x,y)))
            encrypted_image.putpixel((x,y),target_pixel)
    encrypted_image.show()
    files=[('PNG Image', '*.png')]
    file_name = asksaveasfilename(filetypes = files, defaultextension = files)
    encrypted_image.save(file_name)


