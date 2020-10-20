# **Finding Lane Lines on the Road** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />

<h2> Introduction </h2>
  <p>The project focusses on lane dectetion in images as well as in video using OpenCV. The pipeline is as below.
    <UL>
      <LI> The colour image or the video frame is converted into gray scale.</LI>
      <LI> Now a Gaussian Blur is added to the image with a kernel size of 5X5 </LI>
      <LI> Now Canny edge detection algorithm is applied to this image to get the edges in the image. It uses a gradients to find out the edges.</LI>
      <LI> The threshold values are chosen between 50 and 150 </LI>
      <LI> Now we crop the image to get more focus on the road section of the image thereby eliminating the sky areas. <LI/>
      <LI> We use OpenCV fillPoly function to get the mask of the road surface and then bitwise and with the image from Canny. </LI>
      <LI> Now we have the edges of the roads and we need to connect the nearby edges to get the lanes </LI>
      <LI> We use Hough transform to get the lines with the parameters.</LI>
        <UL>
          <LI> rho=2  </LI>
          <LI> theta=pi/180 </LI>
          <LI> thresh=36 </LI>
          <LI> min_line_length=38 </LI>
          <LI> max_line_gap=43 </LI>
        </UL>
  </UL>
  </p>




