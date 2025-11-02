import numpy as np
from PIL import Image
from argparse import ArgumentParser


args = ArgumentParser()

args.add_argument("--source")
args.add_argument("--destination")

params = args.parse_args()

source_image = Image.open(params.source)
destination_image = Image.open(params.destination)

np.asarray(source_image)



