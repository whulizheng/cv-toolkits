from typing import Any
import numpy as np

class GaussianNoise():
    def __init__(self,mean=0, sigma=25) -> None:
        self.mean = mean
        self.sigma = sigma
    def __call__(self, image) -> Any:
        gauss = np.random.normal(self.mean,self.sigma,image.shape)
        image = image + gauss
        image = np.clip(image,a_min=0,a_max=255)
        return image
