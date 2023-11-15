import numpy as np
import os
from PIL import Image


from PIL import Image  
import numpy as np

def numpy_to_pil(image):
    image = Image.fromarray(np.uint8(image))
    return image

def save_image(image,path):
    if  os.path.isdir(os.path.split(path)[0]):
        pass
    else:
        os.mkdir(os.path.split(path)[0])
    if isinstance(image,np.ndarray):
        image = numpy_to_pil(image)
    image.save(path)


def load_image(path):
    return np.array(Image.open(path))

def preprocess(inp):
    out = []
    if isinstance(inp,str):
        if os.path.isfile(inp):
            dic = {
                "data":load_image(inp),
                "root":os.path.split(inp)[0],
                "dir":"",
                "name":os.path.split(inp)[1]
            }
            out.append(dic)
        elif os.path.isdir(inp):
            for root, dirs,files in os.walk(inp):
                for f in files:
                    dic = {
                "data":load_image(os.path.join(root,f)),
                "root":inp,
                "dir":root[len(inp):],
                "name":f
            }
                    out.append(dic)
        else:
            print("Wrong Path {}".format(inp))
            exit(-1)
    else:
        print("Wrong Path {}".format(inp))
        exit(-1)
    return out