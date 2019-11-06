## Writeup

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: undistort.jpg "Undistorted"
[image2]: warped_binary.jpg "Warped Binary Image"
[image3]: binary.jpg "Binary Example"
[image4]: warped_reg.jpg "Warp Original Example"
[image5]: final.jpg "Final Image"
[image6]: final4.jpg "Final Output"
[video1]: output1_tracked.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---


### Camera Calibration

The code for this step is contained in the first code cell of the IPython notebook located in "AdvancedLaneLines.ipynb".  

The findChessBoardCorners and calibrateCamera functions from the OpenCV library are the primary tools for the image calibration. I first convert the image to grayscale before passing the image to the 'findChessboardCorners' function.  I then prepare "object points", which will be the (x, y, z) coordinates of the chessboard corners. I assume the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  For some of the images, the findChessboardCorners function is not able to detect the proper amount of internal corners. Those images are ignored for calibration.  

As I iterate through each of the images I append the object points and corners found to the 'objpoints' and 'imgpoints' arrays respectiveyly. These variables are passed into the 'calibrateCamera' function from OpenCV to calibrate the camera. The results are then saved, with select results being used later in the project.

#### Example of a distortion-corrected image.
I applied the distortion correction to the test image below using the 'undistort' function from the OpenCV libary. The most obvious distinction between the original and undistorted image can be seen by observing the left tail light of the white car. 

![alt text][image1]

### Pipeline (single images)

I applied sobel gradient thresholds and color channel threshold to generate a binary image. These functions are the first 2 functions in the General Functions section of the iPython notebook. The following is a sample of a binary image created by this process:

![alt text][image3]

#### Description of perspective transform.

The code for my perspective transform is in a function called 'get_warped' which is in the General Functions cell of the iPython notebook. The function accepts a binary image as input and outputs a warped image. I attempted to set the source points based on input image size, but struggled with getting it to work as good as just hard coding the points. In the end, I used the following hard coded source points and was able to base destination points on the image size and a standard offset (also below):

```python
    offset = 350

    src = np.float32([[[ 610,  450]], 
                      [[ 680,  450]], 
                      [[ 980,  680]],
                      [[ 380,  680]]])

    # Result points        
    dst = np.float32([[offset, 0], 
                    [img_size[0]-offset, 0], 
                    [img_size[0]-offset, img_size[1]], 
                    [offset, img_size[1]]])  
```
The following are the original test images after applying warp:
![alt text][image4]

The following are the binary images after applying warp:

![alt text][image2]

#### Identifying Lane-line Pixels and Fit with a Polynomial?

I used the warped images to find the lane line pixels and fit a polynomial to each of the lane lines.  The code for this is in the 'class_tracker' function under the Find Lane Lines Functions in the iPython Notebook.

After the lane lines were found, I overlayed the lines on to the original image and filled in the space with the color green. The final images are as follows:

![alt text][image5]

#### Calculating the Radius of Curvature of the Lane and the Position of the Vehicle.

The functionality for calculating the radius of curvature of the lane, along with position of the vehicle with repect to center, can be found in the 'curve' function under the Find Lane Line Functions section of the iPython notebook.  

The radius of the curvature is based on the coefficients of the second order polynomial fit. I then use the following variables for converting from pixels to meters:
    
    
    ym_per_pix = 30/720 # meters per pixel in y dimension
    xm_per_pix = 3.7/700 # meters per pixel in x dimension

The position of the vehicle is determined by taking the average of the x intercepts of each line.

#### Result Plotted Onto the Road.

The final steps are to draws the lanes on to the warped blank image and then warp that image on to the original image. The functionality is in lines 87-92 of the 'process_image' function.

Below is a sample of the result plotted back down onto the road. I have also included all 6 of the "final" images where lanes have been highlighted on road in the project zip.

![alt text][image6]

---

### Pipeline (video)

Here's a [link to my video result][video1]
---

### Discussion

I encountered no major problems with this project since it is an accumulation of work that we have already completed in this course, along with some new twists. It did take me a while to 'put it all together' where some of my original attempts veered far to the left. For the most part, it was a matter of making sure all of the calculations (of which there are many) had the correct attributes.

Due to time/processor constrains, I was not able to test my solution on more difficult roads. I do plan to do that, but not until after submitting this project. I am guessing there may be improvements required in order to handle more extreme curves and road conditions to make this fairly basic model.

One point where I noticed the video had minor issues is when going over bridges. I am inclined to attibute this to the bridge road being a different color (pavement vs. asphalt), but there could also be minor issues due to horizontal cracks at beginning and end of road. Assuming the problem is related to color of road, it can most likely be corrected by tweaking various color functions.
