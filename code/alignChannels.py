import numpy as np
import sys

def alignChannels(red, green, blue):
    """Given 3 images corresponding to different channels of a color image,
    compute the best aligned result with minimum abberations

    Args:
      red, green, blue - each is a HxW matrix corresponding to an HxW image

    Returns:
      rgb_output - HxWx3 color image output, aligned as desired"""

    # fix red, shift green and blue to find min SSD
    greenSSDmin = sys.maxsize
    blueSSDmin = sys.maxsize
    greenIdx = [0,0]
    blueIdx = [0,0]
    for i in range(-30, 30):
      for j in range(-30, 30):
        greenSSD = calculateSSD(red, np.roll(green, [i, j], axis = [1, 0]))
        blueSSD = calculateSSD(red, np.roll(blue, [i, j], axis = [1, 0]))
        if greenSSD < greenSSDmin:
          greenSSDmin = greenSSD
          greenIdx = [i, j]
        if blueSSD < blueSSDmin:
          blueSSDmin = blueSSD
          blueIdx = [i, j]
    return np.stack([red, 
    np.roll(green, greenIdx, axis = [1, 0]), 
    np.roll(blue, blueIdx, axis = [1, 0])], axis = 2)

def calculateSSD(u, v):
  return np.sum(pow(u-v, 2))