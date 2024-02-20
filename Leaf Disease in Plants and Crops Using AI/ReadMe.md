# Project Description: Leaf Disease Detection Using AI

## Introduction:
Welcome to the world of leaf disease detection using artificial intelligence (AI)! This project is dedicated to utilizing the power of AI to detect and diagnose diseases in plant leaves. By harnessing the capabilities of deep learning, we aim to create a robust and accurate system capable of identifying various diseases that affect plant health.

## Objective:
The primary objective of this project is to develop an AI-powered solution for detecting leaf diseases in plants. By analyzing images of plant leaves, the system will be able to identify the presence of diseases and provide timely recommendations for treatment. This project aims to empower farmers and agricultural professionals with a tool that can help them monitor and manage plant health more effectively.

## Dataset:
The dataset for this project consists of images of plant leaves affected by various diseases. These images have been carefully curated and labeled to facilitate training of the AI model. The dataset includes samples of leaves affected by common diseases such as leaf rust, powdery mildew, and bacterial spot, among others.

## Python Version:
This project is developed using Python 3.11.6, ensuring compatibility with the latest features and functionalities of the Python programming language.

## Project Structure:
The project is organized into the following directories and files:
- **static:** Contains static files such as images or CSS stylesheets (if applicable).
- **templates:** Stores HTML templates for rendering dynamic content (if applicable).
- **test:** A directory for storing any test-related files or scripts.
- **main.py:** The main Python script for running the leaf disease detection system. This script serves as the entry point for interacting with the AI model and processing leaf images for disease detection.
- **Trained_model.h5:** A pre-trained deep learning model stored in the Hierarchical Data Format (HDF5) format. This model has been trained on the provided dataset and is ready for use in detecting leaf diseases.
- **Training.ipynb:** A Jupyter Notebook containing the code for training the deep learning model. This notebook provides detailed explanations and examples of how the model was trained, allowing users to gain insights into the training process and potentially retrain the model with their own data.

## Usage:
To use the leaf disease detection system, follow these steps:
1. Download the dataset and pre-trained model from the provided [Google Drive link](https://drive.google.com/drive/folders/1mmQ8qVRLhxxgIG1qCWIAsDNwyb6xa4fQ?usp=share_link).
2. Place all files and directories in the appropriate structure within your project directory.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the leaf disease detection system:
```bash
python main.py
