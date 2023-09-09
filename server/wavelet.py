#This file is actually storing the wavelet function which we used at the time of model training
# This actually getting an image and returning the wavelet transform of that image in return

# importing wavelet transform library pywt, numpy and cv2

import numpy as np
import pywt
import cv2


# wavelet transfromation function
def w2d(img, mode='haar', level=1):
    imArray = img
    # Datatype conversions
    # convert to grayscale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    # convert to float
    imArray = np.float32(imArray)
    imArray /= 255;
    # compute coefficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # Process Coefficients
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;

    # reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)

    # returning a new image which is our wavelet transform
    return imArray_H
