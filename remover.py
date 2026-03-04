import rembg
from PIL import Image

def remove_background(img_path):
    
    img = Image.open(img_path)
    result = rembg.remove(img)
    result.save('Output.png')
    
    return result


