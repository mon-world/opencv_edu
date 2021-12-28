import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg', 1)

scalingFactor = 1 / 255.0

source = source * scalingFactor

print(source)

print(source.max())
print(source.min())

# Convert back to unsigned int (8bit)

source = source * (1.0 / scalingFactor)

# source = source.astype('uint8')

source = np.uint8(source)

print(source)

print(source.dtype)