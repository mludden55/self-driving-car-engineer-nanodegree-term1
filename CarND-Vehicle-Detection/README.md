

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: output_images/random_car.jpg
[image2]: output_images/random_notcar.jpg
[image3]: output_images/image_heat_rectangles.jpg
[image4]: output_images/image_threshold_rectangles.jpg
[image5]: output_images/image_heat.jpg
[image6]: output_images/image_threshold.jpg
[image7]: output_images/image_threshold_rectangles.jpg
[image8]: output_images/image_rectangles.jpg
[video1]: output_images/test_video_out.mp4

## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Histogram of Oriented Gradients (HOG)

#### 1. Extracting HOG features from training images

The code for this step is contained in the Support Functions cell of the iPython Notebook. I basically used the function provided in class, with minor modifications related to version updates.

I first read in all of the `car` and `not car` images. I then passed the images to the get_hog_features function and displayed both the original image and HOG image so I could get a better understanding of what the HOG image looked like. Here is a random sample of 6 car and not car images with their related HOG images:

![alt text][image1]
![alt text][image2]

I then applied different parameters; parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two types of images and displayed them to get a feel for what the HOG output looks like.

The above examples used the `YUV` color space and HOG parameters of `orientations=11`, `pixels_per_cell=(16, 16)` and `cells_per_block=(2, 2)`:



#### 2. Explain how you settled on your final choice of HOG parameters.

My final choice of HOG parameters was based on trial and error when running the process to find cars in images. Different combinations could have very different results. Given more time, I am confident that I could fine tune the parameters to provide much better accuracy. However, the parameters used do a pretty good job when processing the video.

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I trained a linear SVM the same parameters described above. In addition, I passed the hog_channel in as "ALL", which seemed to give the best results when trying to find vehicles.

### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

I based my sliding windows functionlity on some code I found in Jeremy Shannons git repository (https://github.com/jeremy-shannon/CarND-Vehicle-Detection). I added the sliding windows into the "get_cars2" function where much of the processing takes place. I then used a mix of ystart and ystop values, along with different scales in the range of 1.0 to 2.0. 

Here is a sample of a couple sliding windows searches:
![alt text][image8]

#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

After running the images through the functionality to find varous rectangles, I processed the images further by applying heatmap and thresholding to the images. Here are samples of images where heatmap only was applied vs. thresholidng in addtion to heatmap:

![alt text][image3]
![alt text][image4]
---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](test_video_out.mp4)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  As mentioned above, I applied both heatmap and thresholding to identify vehicle positions. I then used the heatmap/threshold image to identitify the vehicles. I assumed each blob corresponded to a vehicle and created bounding boxes to cover the area of each blob detected.


### Here are 2 of the test images with heatmap only and heatmap with thresholding applied: A fairly minor difference that had a significant impact on results.

![alt text][image5]

![alt text][image6]

### Here  is the resulting bounding boxes drawn onto the last 2 test images:
![alt text][image7]



---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

The biggest problem I faced was matching the image input parameters to the various colorspace. I ran into some problem sizing the input just right so as to not cause errors. I am guessing the biggest problem would be false positives related to stop signs and similar objects that are shaped like a car. To a lesser degree curving road and hills would likely throw it off.

