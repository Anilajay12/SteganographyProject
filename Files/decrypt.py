from PIL import Image,ImageDraw
import PIL


def processInts(n1):
    n1_as_string=str(n1)
    n1_as_string='0'*(3-len(n1_as_string))+n1_as_string
    n1_as_string=n1_as_string[-1:-3:-1]+'0'
    final_value=int(n1_as_string)
    return final_value



def peelPixel(pixel):

    pixel_n=(processInts(pixel[0]),processInts(pixel[1]),processInts(pixel[2]))
    return pixel_n



def decryptImage(encrypted_image):
    width,height=encrypted_image.size
    decrypted_image = Image.new('RGB', (width,height), color = 'red')
   
    for x in range(width):
        for y in range(height):
            source_pixel=encrypted_image.getpixel((x,y))
            target_pixel=peelPixel(source_pixel)
            decrypted_image.putpixel((x,y),target_pixel)
            
    decrypted_image.show()
    decrypted_image.save('decrypted_image.png')
