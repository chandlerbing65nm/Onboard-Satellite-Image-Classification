# Onboard Satellite Image Classification
This repo is based on my project for image classification of satellite images onboard a nanosatellite.

# Introduction
I designed the software used to classify Earth, Space and Sun-Flare images onboard a nanosatellite. Its purpose is to optimize the bandwidth used in sending the data to the ground station during downlink.

# Installation
### Requirements
- Linux/Windows/Mac
- Python 3
### Dependencies
    pip install -r requirements.txt
    
# Getting Started
### Training and Inference
Run the [model.py](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/model.py) to start the training and testing process. The result will give an output file of [ICU_model.h5](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/tree/main/Models) and a lite version [model_tflite](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/tree/main/Models).
```
python model.py
```
# Demo
### Earth
![alt text](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Dataset/Test/Earth/BIRDS3-1-1.jpg)
### Sun Flare
![alt text](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Dataset/Test/Flare/NanoSat-20.jpg)
### Space
![alt text](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Dataset/Test/Space/D2_MFC_2019-02-27T191956086_%5B000.000%5D-thumb.jpg)
