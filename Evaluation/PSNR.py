from typing import Any
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

class PSNR():
    def __init__(self) -> None:
        pass
    def __call__(self, image_0,image_1) -> Any:
        score = compare_psnr(image_0,image_1)
        return score