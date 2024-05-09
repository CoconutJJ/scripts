from PIL import Image
import numpy as np

data = np.genfromtxt("data.txt", dtype=np.uint8, delimiter="\t")[:-1]
print(data.shape)
data = data.reshape((683, 683, 3))
Image.fromarray(data).save("out.png", format="PNG")
