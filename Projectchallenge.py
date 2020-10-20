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
cap=cv2.VideoCapture('./test_videos/challenge.mp4')
#cap=cv2.VideoCapture('./test_videos/solidWhiteRight.mp4')
#cap=cv2.VideoCapture('./test_videos/solidYellowLeft.mp4')
size=(int(cap.get(3)),int(cap.get(4)))
result = cv2.VideoWriter('./Output/challenge.mp4',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 

#result = cv2.VideoWriter('./Output/solidWhiteRight.avi',  
#                         cv2.VideoWriter_fourcc(*'MJPG'), 
#                         10, size) 

#result = cv2.VideoWriter('./Output/solidWhiteRight.avi',  
#                         cv2.VideoWriter_fourcc(*'MJPG'), 
#                         10, size) 
#cv2.imshow('image',image)
while(1):
    ret, image = cap.read()
    if ret:
        gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray_image)
    
        kernel_size=5
        blur_gray= cv2.GaussianBlur(gray_image,(kernel_size,kernel_size),0)
        #low=50
        #high=150
    #Below one for challenge
        low=200
        high=220
        edges=cv2.Canny(blur_gray,low,high)
#cv2.imshow('edges',edges)


        mask = np.zeros_like(edges)
        imshape=image.shape
    #Below one is for challenge
        vertices = np.array([[(0,imshape[0]),(680,400),(720,400),(imshape[1],imshape[0])]],dtype=np.int32)
    #vertices = np.array([[(0,imshape[0]),(500,310),(520,310),(imshape[1],imshape[0])]],dtype=np.int32)
        cv2.fillPoly(mask,vertices,255)
        masked_edges=cv2.bitwise_and(edges,mask)
        cv2.imshow('mask',masked_edges)

        rho=2
        theta=np.pi/180
        thresh=60
        min_line_length=40
        max_line_gap=30
        line_image = np.copy(image)*0
        lines = cv2.HoughLinesP(masked_edges,rho,theta,thresh,np.array([]),min_line_length,max_line_gap)

        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

        color_edges=np.dstack((edges,edges,edges))
    #lines_edges=cv2.addWeighted(color_edges,0.8,line_image,1.0,0)
        lines_edges=cv2.addWeighted(image,0.8,line_image,1.0,0)
        lines_edges=cv2.cvtColor(lines_edges,cv2.COLOR_BGR2RGB)
        result.write(lines_edges)
        cv2.imshow('lines',lines_edges)
    #k = cv2.waitKey(1) & 0xFF
    #Press q ti exit
        if cv2.waitKey(1) & 0xFF == ord('q'): 
        
            break
    else:
        break
        

#closing all open windows
cap.release()  
result.release() 
cv2.destroyAllWindows() 