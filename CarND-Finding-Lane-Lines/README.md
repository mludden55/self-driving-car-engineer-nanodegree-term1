# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:

1. Create a pipeline that finds lane lines on a road contained on an image.
2. Apply the pipeline to videos in order to identify lane lines on a moving road.

---

## Reflection

### My pipeline consists of 7 steps:

1. Convert the input image to grayscale.

2. Smooth the image using Gaussian Blur.

3. Find the edges on the image using the Canny method.

4. Define a 4 sided polygon that focuses in on the roadway.

5. Uses the Hough method to determine where the lines are within the 4 sided polygon. This method also includes a call to the draw\_lines function. The draw\_lines function:

      A. Loops over the lines to sum their coordinates and determine the slope.

      B. Use the slope to determine if it is the left or right line.

      C. Find the average slope and coordinates of each line in order to draw the line.

      D. Draw the line. 
   
6. Apply the lines created above on to the original image using the cv2.addWeighted method.

7. Output the image for viewing and save it to the local file system.


### Potential Shortcomings With My Current Pipeline
1. The lines are a bit shaky when applied to video and could be much worse on additional test videos.
2. The lines should be extended further out.
3. The lines will most likely not work on roads with a lot of curves.

### Possible Improvements to My Pipeline
1. Reduce shakiness.
2. Bend the lines along with the road.
3. Test and code for additional color schemes (very light lines, etc) along with extended breaks in lines.



