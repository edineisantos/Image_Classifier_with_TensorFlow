# Image Classifier - TensorFlow Project

Project code for Udacity's Intro to Machine Learning with TensorFlow Nanodegree program.

## Project Description

This project is ...

## Objectives

This project aims to demonstrate the following competencies:

* Writing modular and maintainable code.
* Adherence to PEP8 coding standards.
* Implementation and execution of unit tests.

## Files and Data Description

Overview of the folders, files, and data present in the root directory.

- **.gitignore** ...
- **predict.py:** Library of functions for identifying customers likely to churn.
- **Project_Image_Classifier_Project.ipynb:** notebook where the model of `predict_library.py` was developed.
- **Project_Image_Classifier_Project.html:** notebook where the model of `predict_library.py` was developed in html.
- **Dockerfile:** Instructions for building the Docker image required to run the project.
- **README.md:** Project overview and setup instructions.
- **requirements.txt:** List of dependencies and libraries required to run the project.

### Folders in the Root Directory:
- **assets**: Dataset used for the project.
- **test_images**: Dataset used for the project.

### Files in the Image/EDA Folder:
- **churn_distribution.png**: Visualization showcasing the distribution of customer churn.
- **customer_age_distribution.png**: Histogram displaying the distribution of customers' ages.
- **heatmap.png**: A heatmap showing the correlation matrix of the different features in the dataset.
- **marital_status_distribution.png**: Bar chart displaying the distribution of customers based on their marital status.
- **total_transaction_distribution.png**: Visualization depicting the distribution of the total transactions made by customers.

## Dataset

oxford_flowers102

## Running the Project

This section provides guidelines for building and running the Docker image, as well as for executing the project's Python scripts.

### Building and Running the Docker Image

1. Open your terminal and navigate to the project's root directory, where the `Dockerfile` is located.

2. Build the Docker image by running the following command:
    ```bash
    docker build -t predict_customer_churn_image .
    ```

3. After the image has been built successfully, you can run a Docker container based on this image with a specified name:
    ```bash
    docker run -it --name predict_customer_churn_container --rm predict_customer_churn_image
    ```

Note: The `--name` flag assigns a name to the running container, which is `predict_customer_churn_container` in this example. The container will provide an interactive shell. From there, you can navigate to the appropriate directories within the container to run the Python scripts or notebooks.

### Running Scripts with IPython

#### churn_library.py
To run the `churn_library.py` script, follow these steps:

1. Open your terminal and navigate to the project's root directory.

2. Start IPython and run the script by entering the following command:
    ```bash
    ipython churn_library.py
    ```

#### churn_script_logging_and_tests.py
To run the `churn_script_logging_and_tests.py` script, you'll also want to be in the project's root directory.

1. Make sure you're in the terminal and start IPython with the script by entering:
    ```bash
    ipython churn_script_logging_and_tests.py
    ```

By following these steps, you can successfully build the Docker container, and run the `churn_library.py` and `churn_script_logging_and_tests.py` scripts using IPython.

