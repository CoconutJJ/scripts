import numpy as np
from PIL import Image

img = np.random.randint(0, 125, size=(768, 768, 3)).astype(np.uint8)

Image.fromarray(img).save("out.png", format="PNG")
