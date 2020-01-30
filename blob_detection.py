
import sys
import cv2
import numpy as np 

# kernel = np.ones((3,3),np.uint8)

# lower = np.array([ 165.,   100.,  100.])
# upper = np.array([ 185., 220., 210.])



# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, lower, upper)
# mask = cv2.bilateralFilter(mask,9,75,75)
# mask = cv2.dilate(mask,kernel,iterations=1)

# # cv2.imshow("mask",mask)
# _, contours, hR = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# idx,current_max,counter = 0, 0, 0	
# for n in contours:
# 	a = cv2.contourArea(n)
# 	if a>current_max:
# 		current_max=a
# 		idx = counter
# 	counter+=1


# redIndex, redValue = idx, current_max

#Visulization
# cv2.drawContours(frame, contours, idx, (0, 0, 255), 2)

#For contour based centroid

#Get contour array
# cimg = np.zeros_like(frame)
# cv2.drawContours(cimg, contoursRed, redIndex,(0,0,255),2)
# pts = np.where(cimg==255)
# # pts_pc2 = ros_numpy.point_cloud2.array_to_pointcloud2(pts)

# pts = np.array(pts)
# print(pts.shape)
# c_row = np.mean(pts[:,0])
# c_col = np.mean(pts[:,1])
# arr = [c_row, c_col]

#For bounding-box based centroid
# x,y,w,h = cv2.boundingRect(contours[idx])
# c_x = (x + w/2)
# c_y = (y + h/2)
# arr = [c_x,c_y]
# print(arr)
# centroid_pub.publish(arr)
# img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imshow(node_name, frame)
# # pc2_pub.publish(pts_pc2)
# if cv2.waitKey(10) == ord('x'):
# 	cv2.DestroyAllWindows()
		

def get_blob(cap):

	print("Press Enter to freeze frame")
	while(1):
		ret, frame = cap.read()
		cv2.imshow('video', frame)
		if cv2.waitKey(10) == ord('13'):
			bbox = cv2.selectROI(frame)
			obj = hsv[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]

			h, s, v = np.median(obj[:,:,0]), np.median(obj[:,:,1]), np.median(obj[:,:,2])
			lower = np.array([ h-10,   min(0,s-100),  min(0,v-100)])
			upper = np.array([ h+10,  max(s+100,255),  max(v+100,255)])
			return(lower, upper)

if __name__ == '__main__':

	
	cap = cv2.VideoCapture(2)
	lower, upper = get_blob(cap)
	print(lower, upper)
	# while(1):
	# 	detect_blob()