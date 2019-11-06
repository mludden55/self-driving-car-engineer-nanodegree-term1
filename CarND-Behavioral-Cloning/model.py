# import libraries to use for this project
import csv
import cv2
import numpy as np
import os
from sklearn.cross_validation import train_test_split 
from sklearn.utils import shuffle
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout, ELU
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.models import Sequential
from keras.models import Model
from keras.callbacks import ModelCheckpoint

# Function for randomizing brightness of images
def preprocess_image(image):
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    default_bias = 0.25
    brightness = default_bias + np.random.uniform()
    new_image[:, :, 2] = new_image[:, :, 2] * brightness
    new_image = cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)
    new_image = cv2.GaussianBlur(new_image, (3,3), 0)

    return new_image

#function for traing the data
def generate_training_data(x_data, y_data, batch_size):
    x_data, y_data = shuffle(x_data, y_data)
    x_train,y_train = ([],[])
    while True:       
        for i in range(len(y_data)):
            image_train = preprocess_image(x_data[i])
            measurement_train = y_data[i]
            x_train.append(image_train)
            y_train.append(measurement_train)

            if len(x_train) == batch_size:
                yield (np.array(x_train), np.array(y_train))
                x_train, y_train = ([],[])
                x_data, y_data = shuffle(x_data, y_data)


# Read training data from the csv file and add to lines array
lines = []
with open('data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)        
    for line in reader:
        speed = float(line[6])
		
        if speed < .1:
            continue



        lines.append(line)
        
# Initialize variables
images = []
measurements = []
correction = 0.25

# Loop through lines array
for line in lines:
    for i in range(3):
        # Set path for reading in the image
        source_path = line[i]
        tokens = source_path.split('/')
        filename = tokens[-1]
        current_path = 'data/IMG/' + filename

        # ** Note that I had to read image via absolute path in order for random image brightness to work on AWS
        new_path = os.path.abspath(current_path)
        image = cv2.imread(current_path)
        image = preprocess_image(image)
        images.append(image)
        measurement = float(line[3])

		# Add correction based on which camera image we are using
        if i == 0:
                measurements.append(measurement)
        elif i == 1:
                measurements.append(measurement+correction)
        else:
                measurements.append(measurement-correction)
        
print('Reading of data is complete')

x_array = np.array(images)
y_array = np.array(measurements)

# split the data for training and validation
x_array, x_validation, y_array, y_validation = train_test_split(x_array, y_array, test_size= 0.1, random_state = 3)


# Build the model
model = Sequential()
model.add(Lambda(lambda x: x / 127.5 - 1.0, input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((65,30),(0,0))))
model.add(ELU())

model.add(Convolution2D(24,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(ELU())

model.add(Convolution2D(36,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(ELU())

model.add(Convolution2D(48,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(ELU())

model.add(Convolution2D(64,3,3,activation="relu"))
model.add(MaxPooling2D())
model.add(ELU())

model.add(Flatten())
model.add(Dropout(.2))
model.add(ELU())

model.add(Dense(100))
model.add(Dropout(.2))
model.add(ELU())

model.add(Dense(50))
model.add(Dropout(.5))
model.add(ELU())

model.add(Dense(10))
model.add(Dropout(.5))
model.add(ELU())

model.add(Dense(1))

model.compile(loss = 'mse', optimizer='adam')

#train and validate the model
train_generation = generate_training_data(x_array, y_array, 128)
validation_generation = generate_training_data(x_validation, y_validation, 128)

checkpoint = ModelCheckpoint('model{epoch:02d}.h5')

model.summary()

model_run = model.fit(x_array, y_array, validation_split=0.2, shuffle = True, epochs=3)

# Save the model.
model.save('model.h5')
print('Model Saved')

