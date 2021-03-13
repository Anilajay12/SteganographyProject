from tkinter import *
from tkinter.ttk import * # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont
import textwrap
from PIL import Image,ImageDraw
import PIL
import card_creation


def encryptionController(text_message):
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if(filename.endswith('.png')or filename.endswith('.jpg') or filename.endswith('.jpeg')):
        import encrypt
        base_image = Image.open(filename,'r')
        width,height=base_image.size
        print('Encrypting...')
        hidden_image=card_creation.generateImage(text_message,width,height)
        encrypt.encryptImage(base_image,hidden_image)
        
    #Code that is reached when the selected file is not an image
    else:
        print('Please Select a png or a jpeg file')
        
def decryptionController():
    import decrypt
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print('Decrypting...')
    if(filename.endswith('.png') or filename.endswith('.PNG')):
        encrypted_image = Image.open(filename,'r')
        decrypt.decryptImage(encrypted_image)
    else:
        print('Invalid format. Please select only a .png file')


def temp(text):
    print(text)
def openTextMessageWindow():
    newWindow = Toplevel(root)
    newWindow.geometry('510x450')
    wlabel=Label(newWindow,anchor=CENTER,text="Enter the Message to be encrypted below!",font=("Helvetica",13),wrap=320,background='#3498DB',foreground='white')
    wlabel.place(x=0,y=0)
    newWindow.resizable(0,0)
    newWindow.configure(bg = '#3498DB')
    text_entry=Text(newWindow,height=20, width=60,bd=3)
    text_entry.place(x=10,y=60)
    newWindow.title("Crypto Crew")
    b3 = Button(newWindow, text="Click to continue", width = 25,command=lambda:encryptionController(text_entry.get("1.0", "end-1c")))
    b3.place(x=180,y=400)
    



#Designing the Interface.....
root = Tk()
root.geometry('300x200')
root.configure(bg = '#3498DB')
root.resizable(0,0)
root.title("Crypto Crew")

#Placing a Label for Introduction
wlabel=Label(root,anchor=CENTER,text="Hey There! Welome to Steganography Application developed by Crypto Crew",font=("Helvetica",13),wrap=320,background='#3498DB',foreground='white')
wlabel.pack()

#Placing the First Button for Encryption
b1 = Button(root, text="Encrypt into an image", command=openTextMessageWindow)
b1.place(x=90, y=80)

#PLacing the second button for decryption
b2 = Button(root, text="Decrypt from an image", command=decryptionController)
b2.place(x=90, y=120)


root.mainloop()





    
