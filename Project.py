# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:34:39 2020

@author: Admin
"""

import cv2
import numpy as np

#whiteCarLaneSwitch
#solidYellowLeft
#image=cv2.imread('./test_images/solidWhiteCurve.jpg')
#image=cv2.imread('./test_images/solidWhiteRight.jpg')
#image=cv2.imread('./test_images/solidYellowCurve.jpg')
#image=cv2.imread('./test_images/solidYellowCurve2.jpg')
#image=cv2.imread('./test_images/solidYellowLeft.jpg')
image=cv2.imread('./test_images/whiteCarLaneSwitch.jpg')

cv2.imshow('image',image)
 
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray_image)

kernel_size=5
blur_gray= cv2.GaussianBlur(gray_image,(kernel_size,kernel_size),0)
low=50
high=150
edges=cv2.Canny(blur_gray,low,high)
cv2.imshow('edges',edges)


mask = np.zeros_like(edges)
imshape=image.shape
vertices = np.array([[(0,imshape[0]),(500,310),(520,310),(imshape[1],imshape[0])]],dtype=np.int32)
cv2.fillPoly(mask,vertices,255)
masked_edges=cv2.bitwise_and(edges,mask)
cv2.imshow('mask',masked_edges)

rho=2
theta=np.pi/180
thresh=36
min_line_length=38
max_line_gap=43
line_image = np.copy(image)*0
lines = cv2.HoughLinesP(masked_edges,rho,theta,thresh,np.array([]),min_line_length,max_line_gap)

for line in lines:
  for x1,y1,x2,y2 in line:
    cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

color_edges=np.dstack((edges,edges,edges))
#lines_edges=cv2.addWeighted(color_edges,0.8,line_image,1.0,0)
lines_edges=cv2.addWeighted(image,0.8,line_image,1.0,0)
lines_edges=cv2.cvtColor(lines_edges,cv2.COLOR_BGR2RGB)
cv2.imshow('lines',lines_edges)
#cv2.imwrite('./Output/solidWhiteCurve.jpg',lines_edges)
#cv2.imwrite('./Output/solidWhiteRight.jpg',lines_edges)
#cv2.imwrite('./Output/solidYellowCurve.jpg',lines_edges)
#cv2.imwrite('./Output/solidYellowCurve2.jpg',lines_edges)
#cv2.imwrite('./Output/solidYellowLeft.jpg',lines_edges)
cv2.imwrite('./Output/whiteCarLaneSwitch.jpg',lines_edges)
#closing all open windows
cv2.waitKey(0)   
cv2.destroyAllWindows() 


#cv2.imwrite('./Output/solidWhiteRight.jpg',lines_edges)
#cv2.imwrite('./Output/solidYellowCurve.jpg',lines_edges)
#cv2.imwrite('./Output/solidYellowCurve2.jpg',lines_edges)
#cv2.imwrite('./Output/solidYellowLeft.jpg',lines_edges)
#cv2.imwrite('./Output/whiteCarLaneSwitch.jpg',lines_edges)