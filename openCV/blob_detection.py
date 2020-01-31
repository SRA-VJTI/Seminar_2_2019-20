import numpy as np
import cv2

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    while(1):
        ret, frame = cap.read()
        cv2.imshow("Image", frame)
        if cv2.waitKey(10) == ord('x'):

            bbox = cv2.selectROI(frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            obj = hsv[int(bbox[1]):int(bbox[1] + bbox[3]),
                      int(bbox[0]):int(bbox[0] + bbox[2])]

            h, s, v = np.median(obj[:, :, 0]), np.median(
                obj[:, :, 1]), np.median(obj[:, :, 2])
            lower = np.array([h - 2, min(0, s - 100), min(0, v - 100)])
            upper = np.array([h + 2, max(s + 100, 255), max(v + 100, 255)])
            break

    print(lower, upper)

    while(1):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        masked = cv2.inRange(hsv, lower, upper)
        filtered = cv2.medianBlur(masked, 5, 0)

        coloured_mask = cv2.bitwise_and(frame, frame, mask=masked)

        cv2.imshow("mask", coloured_mask)

        contours, hR = cv2.findContours(
            filtered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        idx, current_max, counter = 0, 0, 0
        for n in contours:
            a = cv2.contourArea(n)
            if a > current_max:
                current_max = a
                idx = counter
            counter += 1

        cv2.drawContours(frame, contours, idx, (0, 0, 255), 2)
        cv2.imshow("Output", frame)
        if cv2.waitKey(10) == ord('x'):
            cv2.destroyAllWindows()
            cap.release()
            break
