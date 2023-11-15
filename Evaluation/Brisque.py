import numpy as np
from brisque import BRISQUE
from PIL import Image
import argparse

class Brisque():
    def __init__(self):
        self.obj = BRISQUE(url=False)
    def __call__(self,image):
        assert type(image) is np.ndarray
        score = self.obj.score(image)
        return score
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path",required=True, type=str,help='image path')
    args = parser.parse_args()
    image_path = args.image_path
    image = np.array(Image.open(image_path))
    brisque = Brisque()
    score = brisque(image)
    print("brisque for image {} is {}".format(image_path,str(score)))