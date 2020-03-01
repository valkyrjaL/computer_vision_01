from alignChannels import alignChannels
from scipy.misc import imsave
import numpy as np
import matplotlib.pyplot as plt
# Problem 1: Image Alignment

# 1. Load images (all 3 channels)
red = np.load("../data/red.npy")
green = np.load("../data/green.npy")
blue = np.load("../data/blue.npy")
misalign = np.stack([red, green, blue], axis = 2)   # with shape of (M, N, 3)

# 2. Find best alignment
rgbResult = alignChannels(red, green, blue)
# plt.imshow(rgbResult)
# plt.show()

# 3. save result to rgb_output.jpg (IN THE "results" FOLDER)
imsave("../results/rgb_output.jpg", rgbResult)