import numpy as np
import cv2


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def convolve(image, kernel):
    # grab the spatial dimensions of the image, along with
    # the spatial dimensions of the kernel
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # allocate memory for the output image, taking care to
    # "pad" the borders of the input image so the spatial
    # size (i.e., width and height) are not reduced

    pad = (kW - 1) // 2
    print(image.shape)
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
                               cv2.BORDER_REPLICATE)
    print(image.shape)
    output = np.zeros((iH, iW), dtype="float32")

    # loop over the input image, "sliding" the kernel across
    # each (x, y)-coordinate from left-to-right and top to
    # bottom
    for y in np.arange(pad, iH + pad):  # change
        for x in np.arange(pad, iW + pad):
            # extract the ROI of the image by extracting the
            # *center* region of the current (x, y)-coordinates
            # dimensions
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            # perform the actual convolution by taking the
            # element-wise multiplicate between the ROI and
            # the kernel, then summing the matrix
            k = (roi * kernel).sum()

            # store the convolved value in the output (x,y)-
            # coordinate of the output image
            output[y - pad, x - pad] = k

    # output = np.clip(output, 0, 255)
    mx = np.amax(output)
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i][j] = translate(output[i][j], 0, mx, 0, 1)

    # return the output image
    return output


# construct a sharpening filter
sharpen = np.array((
    [0, -1, 0],
    [-1, 9, -1],
    [0, -1, 0]), dtype="int")
# construct the Sobel y-axis kernel
edge = np.array((
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]), dtype="int")

image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

convoleOutput = convolve(gray, sharpen)
# opencvOutput = cv2.filter2D(gray, -1, kernel)
cv2.imshow("normal image", gray)
cv2.imshow("filtered image", convoleOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()
