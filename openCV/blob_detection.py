import numpy as np
import cv2

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    while(1):

        # Get the frame from captured camera object and display it
        ret, frame = cap.read()
        cv2.imshow("Image", frame)
        if cv2.waitKey(10) == ord('x'):

            # Select ROI corresponding to colour to be extracted
            bbox = cv2.selectROI(frame)

            # Convert colour space from bgr to hsv
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Extract the corresponding ROI from hsv image and get the median hsv value from the image
            obj = hsv[int(bbox[1]):int(bbox[1] + bbox[3]),
                      int(bbox[0]):int(bbox[0] + bbox[2])]
            h, s, v = np.median(obj[:, :, 0]), np.median(
                obj[:, :, 1]), np.median(obj[:, :, 2])

            # Define the upper and lower limits of the colour to be detected
            lower = np.array([h - 2, min(0, s - 50), min(0, v - 50)])
            upper = np.array([h + 2, max(s + 50, 255), max(v + 50, 255)])
            break

    print(lower, upper)

    while(1):
        ret, frame = cap.read()

        # Convert colour space from bgr to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Thresholding the image
        masked = cv2.inRange(hsv, lower, upper)

        # Blur out the image to remove noise
        blur = cv2.medianBlur(masked, 10, 0)

        # Display coloured mask
        coloured_mask = cv2.bitwise_and(frame, frame, mask=blur)
        cv2.imshow("mask", coloured_mask)

        # Extract contours
        contours, hR = cv2.findContours(
            blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Find the contour with maximum continuous area
        idx, current_max, counter = 0, 0, 0
        for n in contours:
            a = cv2.contourArea(n)
            if a > current_max:
                current_max = a
                idx = counter
            counter += 1

        # Draw contours on original image and display
        cv2.drawContours(frame, contours, idx, (0, 0, 255), 2)
        cv2.imshow("Output", frame)

        # Exit if the key x is pressed
        if cv2.waitKey(10) == ord('x'):
            cv2.destroyAllWindows()
            cap.release()
            break
