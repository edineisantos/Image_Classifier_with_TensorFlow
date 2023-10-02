# Use the official tensorflow image as a parent image
FROM tensorflow/tensorflow:latest-gpu-jupyter

# Make the directory for the project files
RUN mkdir /tf/Image_Classifier_with_TensorFlow

# Set the working directory to /tf
WORKDIR /tf

# Copy the current directory contents into the container
COPY . /tf/Image_Classifier_with_TensorFlow

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt