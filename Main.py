import argparse
import os
import Utils
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--input",required=True, type=str,help='input path')
parser.add_argument("--target",default="", type=str,help='target path')
parser.add_argument("--output",default="", type=str,help='output path')
parser.add_argument("--brisque",action="store_true",help='get brisque score or not')
parser.add_argument("--psnr",action="store_true",help='get brisque psnr or not')
parser.add_argument("--gaussian",action="store_true",help='add gaussian noise or not')
args = parser.parse_args()

inputs = Utils.preprocess(args.input) # process to list of dict of {"data":(np.ndarray [w,h,c] RGB),"root":(str),"dir":(str)}
outputs = []


if args.brisque:
    from Evaluation import Brisque
    brisque = Brisque.Brisque()
    scores = []
    for image in inputs:
        score = brisque(image["data"])
        scores.append(score)
    print("Brisque score is {}".format(np.mean(scores)))

if args.psnr:
    if not args.target:
        print("Please specify the target dir with --target")
        exit(-1)
    from Evaluation import PSNR
    psnr = PSNR.PSNR()
    scores = []
    for image in inputs:
        if os.path.isfile(args.target):
            target_image = Utils.load_image(args.target)
        else:
            target_image = Utils.load_image(os.path.join(args.target,image["dir"],image["name"]))
        score = psnr(image["data"],target_image)
        scores.append(score)
    print("PSNR score is {}".format(np.mean(scores)))


if args.gaussian:
    if not args.output:
        print("Please specify the output dir with --output")
        exit(-1)
    from Degradation import GaussianNoise
    gaussian = GaussianNoise.GaussianNoise()
    print("Output of GaussionNoised images will be save at {}".format(args.output))
    if outputs:
        tmp = []
        for image in outputs:
            dic = {
            "data":gaussian(image["data"]),
            "root":args.output,
            "dir":image["dir"],
            "name":image["name"]
            }
            tmp.append(dic)
        del outputs
        outputs = tmp
        
    else:
        for image in inputs:
            dic = {
            "data":gaussian(image["data"]),
            "root":args.output,
            "dir":image["dir"],
            "name":image["name"]
            }
            outputs.append(dic)

    


if outputs:
    for image in outputs:
        Utils.save_image(image["data"],os.path.join(image["root"],image["dir"],image["name"]))