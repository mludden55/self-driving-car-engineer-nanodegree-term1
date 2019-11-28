# **Traffic Sign Classifier Project** 
Overview
---

The traffic sign classifier project is designed to predict the type of sign for various German traffic signs.  The project starts with a code template provided by Udacity, which I then modified to display various information and increase accuracy of predictions.

Dataset Exploration
---
In order to better understand the data we are dealing with, I first displayed the counts for each of the datasets, along with the number of classes.

I then displayed a graph showing the specific sign counts for each of the datasets.  In general, each of the datasets contain similar percentages for each type of sign.

I then displayed a sample of signs from the training set in order to visualize the data the we are analyzing.  After preprocessing the images (below) I displayed another sample of signs to see the effect that grayscaling had on the images.

Description of Preprocessing
---
Preprocessing consists of the following steps:
1. Shuffle the data
2. Convert image to grayscale
3. Normalize the data

Shuffling the data ensures that the data is treated in a random manner.  I did test the model without shuffling to see if it had any effect on accuracy and it did not.

I expected that converting to grayscale would provide a large increase in accuracy, but the impact was minimal.  I left that functionality in for efficiency purposes.

I tried a couple of different equations for normalizing the data.  The best option appeared to be between .1 and .9. 

Model Architecture
---
For the most part, I used the LeNet architecture provided in the classroom sample. The architecture includes 2 convolutional layers and 3 fully connected layers.  I did tweak it by using average pool instead of max pooling in the convolutional layer.  This change added approximately 2% to the accuracy.  I also added dropout to the fully connected layers, which had a more significant impact in increased accuracy.

Model Training
---
I used the train test split function from sklearn to split the data prior to processing.  I also shuffled the data for each Epoch so that training was not skewed towards a few signs.

I first tested the model by modifying batch size and epochs. A batch size of 64 provided the most accurate results.  The increased accuracy above 20 epochs was minimal, so I set that as the size.

I also tried changing the test_size when splitting data between a value of .005 and .4. .1 provided the best results.

Solution Approach
---
The first modifications I made to the template were the preprocessing part of the program.

Shuffling, adding grayscale and normalizing the image provided the initial increase in accuracy, though not as much as I had hoped for.

The next step I took was to modify various hyperparameters to gauge their impact on accuracy.  At this point, I was still developing on my personal workstation, so I used Epoch value of 3 in order for my workstation to keep the application from timing out.

Once I moved the code to AWS, I increased the Epochs value, testing ranges as high as 50 Epochs.  In the end, there did not seem to be much added value above 20 Epochs.

Similar testing was done with batch size and rate. I ended up using the same rate as the original model, with a lower batch size.

The final changes that I made were to the model itself.  I modified the convolutional layers and fully connected layers as described in the Model Architecture section to get my final boost in accuracy.

Testing Model on New Images
---
Most of the images I found on the internet had high clarity, which led me to believe it would result in a high accuracy.

I originally used the following signs for my testing:
1. Speed Limit Sign
2. Yield
3. Turn Right Ahead
4. No Passing
5. Roundabout Mandatory
6. No Entry

The accuracy rate on these signs was very close to 100%, so the accuracy was in fact high.

I decided to change up to a couple more challenging signs and used the following for my final testing:
1. Speed Limit Sign
2. Turn Right Ahead
3. Double Curve
4. Double Curve
5. Roundabout Mandatory
6. No Entry

I was a bit surprised to find that the accuracy fell to .667 when run on these test images.  This is a decent amount lower than the original images I tested as well as the results of the test set, which was .873.

5 out of the 6 signs have distinct shapes, which I expect would work well with the model.  The other sign, Turn Right Ahead, may be more difficult to predict.

The Roundabout Mandatory sign may also cause problems due the curving arrows inside of the primary shape. Those may be a bit more difficult to read than the others.  I also used 2 double curve signs, with one curving left and then right and the other curving right and then left. While the signs are different, their label is the same.

The Speed Limit and No Entry signs should be predicted with the highest degree of accuracy since they both have a limited amount of distinct shapes.







