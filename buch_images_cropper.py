from PIL import Image     # library for working with images in python 
import os, os.path        # library for getting an ancess to the system directrories
import fnmatch            # library for filterting files

def bunch_crop_images(str_path, str_type, left, top, right, bottom) :
    
    images = fnmatch.filter(os.listdir(str_path), ('*.' + str_type + '*'))
    
    counter = 1
    
    for image in images:
        
        im = Image.open(str_path + "//" + image)
                
        im1 = im.crop((left, top, right, bottom))
        
        if counter < 10:
            
            im1.save(str_path + "//" + "new_" + "0" + str(counter) + ".png")
        
        else:
            
            im1.save(str_path + "//" + "new_" + str(counter) + ".png")
        
        counter = counter + 1
        
    return "Done!!!"

# Example

str_path = r'C:\Users\user1234\Pictures\Screenshots'

str_type = 'png'

left, top = 1, 157 # in pixels

right, bottom = 799, 1222 # in pixels

bunch_crop_images(str_path, str_type, 
                 left, top,
                 right, bottom)
