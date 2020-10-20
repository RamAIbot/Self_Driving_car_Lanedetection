# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:40:29 2020

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:34:39 2020

@author: Admin
"""

import cv2
import numpy as np

#Values
#solidWhiteRight
#rho=2
#theta=28*np.pi/180
#thresh=18
#min_line_length=16
#max_line_gap=50

image=cv2.imread('./test_images/solidYellowLeft.jpg')
#cv2.imshow('image',image)
 
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray_image)

kernel_size=5
blur_gray= cv2.GaussianBlur(gray_image,(kernel_size,kernel_size),0)
low=50
high=150
edges=cv2.Canny(blur_gray,low,high)
#cv2.imshow('edges',edges)


mask = np.zeros_like(edges)
imshape=image.shape
vertices = np.array([[(0,imshape[0]),(500,310),(520,310),(imshape[1],imshape[0])]],dtype=np.int32)
cv2.fillPoly(mask,vertices,255)
masked_edges=cv2.bitwise_and(edges,mask)
#cv2.imshow('mask',masked_edges)

def nothing(x):
  pass
def hough(rho,theta,thresh,min_line_length,max_line_gap):
  # rho=2
  # theta=np.pi/180
  # thresh=15
  # min_line_length=40
  # max_line_gap=30
  print('Here')
  line_image = np.copy(image)*0
  lines = cv2.HoughLinesP(masked_edges,rho,theta,thresh,np.array([]),min_line_length,max_line_gap)

  for line in lines:
    for x1,y1,x2,y2 in line:
      cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

  color_edges=np.dstack((edges,edges,edges))
  lines_edges=cv2.addWeighted(color_edges,0.8,line_image,1.0,0)
  lines_edges=cv2.cvtColor(lines_edges,cv2.COLOR_BGR2RGB)
  cv2.imshow('hough',lines_edges)
  return
  
  

cv2.namedWindow("Hough_Trackbar")

cv2.createTrackbar('Rho','Hough_Trackbar',1,100,nothing)
cv2.createTrackbar('Theta','Hough_Trackbar',1,50,nothing)
cv2.createTrackbar('Thresh','Hough_Trackbar',1,100,nothing)
cv2.createTrackbar('Min_line_length','Hough_Trackbar',1,100,nothing)
cv2.createTrackbar('Max_line_gap','Hough_Trackbar',1,100,nothing)
while(1):
    print('while')
    r=cv2.getTrackbarPos('Rho','Hough_Trackbar')
    t=cv2.getTrackbarPos('Theta','Hough_Trackbar')
    th=cv2.getTrackbarPos('Thresh','Hough_Trackbar')
    ll=cv2.getTrackbarPos('Min_line_length','Hough_Trackbar')
    lg=cv2.getTrackbarPos('Max_line_gap','Hough_Trackbar')
    t=t*np.pi/180
    rho = r
    theta = t
    thresh = th
    min_line_length = ll 
    max_line_gap = lg
  
    line_image = np.copy(image)*0
    lines = cv2.HoughLinesP(masked_edges,rho,theta,thresh,np.array([]),min_line_length,max_line_gap)

    for line in lines:
        
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

    color_edges=np.dstack((edges,edges,edges))
    lines_edges=cv2.addWeighted(color_edges,0.8,line_image,1.0,0)
    lines_edges=cv2.cvtColor(lines_edges,cv2.COLOR_BGR2RGB)
    cv2.imshow('hough',lines_edges)
  

#closing all open windows
    cv2.waitKey(1)   
cv2.destroyAllWindows() 