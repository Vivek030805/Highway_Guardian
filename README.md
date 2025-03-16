# Accident Detection System

**Last Updated: *7 June 2022***

1. Demonstration
2. What is Accident Detection System?
3. Prerequisites
4. Description
5. Future Work

## 1. Demonstration

![Demo](https://user-images.githubusercontent.com/54409969/173066273-732f7da9-8645-4809-aa7a-bb2f78548b3e.gif)

## 2. What is Accident Detection System?

An accident Detection System is designed to detect accidents via video or CCTV footage. Road accidents are a significant problem for the whole world. Many people lose their lives in road accidents. We can minimize this issue by using CCTV accident detection. This repository majorly explores how CCTV can detect these accidents with the help of Deep Learning.

## 3. Prerequisites

- To use this project Python Version > 3.6 is recommended.
- To contribute to this project, knowledge of basic python scripting, Machine Learning, and Deep Learning will help.

## 4. Description

This program includes 4 things.

1. `data`: Kaggle dataset on [Accident Detection from CCTV footage](https://www.kaggle.com/code/mrcruise/accident-classification/data).
2. `accident-classification.ipynb`: This is a jupyter notebook that generates a model to classify the above data. This file generates two important files `model.json` and `model_weights.h5`.
3. `detection.py`: This file loads the Accident Detection system with the help of `model.json` and `model_weights.h5` files.
4. `camera.py`: It packs the camera and executes the `detection.py` file on the video dividing it frame by frame and displaying the percentage of the prediction in the accident (if present) in the frame.
5. An app for end users to know all the things about the accident 

## 5. Future Work

Number plate recognition to fetch out accident victims to let their family know all the things about the accident through the highway guardian app.
