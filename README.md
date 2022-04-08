<p align="center">
  <img 
    width="800"
    height="120"
    src="https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Onboard_Satellite__nImage_Classification.png?raw=true"
  >
</p>

<div align="center">

  <a href="">![last commit](https://img.shields.io/github/last-commit/chandlerbing65nm/Onboard-Satellite-Image-Classification)</a>
  <a href="">![repo size](https://img.shields.io/github/repo-size/chandlerbing65nm/Onboard-Satellite-Image-Classification)</a>
  <a href="">![watchers](https://img.shields.io/github/watchers/chandlerbing65nm/Onboard-Satellite-Image-Classification?style=social)</a>

</div>

<h4 align="center">Image classification of satellite images onboard a nanosatellite..</h4>

# Contents
* [Introduction](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification#Introduction)
* [Installation](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification#Installation)
* [Getting Started](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification#Getting-Started)
* [Demo](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification#Demo)
* [License](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification#License)

# Introduction
I designed the software used to classify Earth, Space and Sun-Flare images onboard a nanosatellite. Its purpose is to optimize the bandwidth used in sending the data to the ground station during downlink.

# Installation
### Requirements
- Linux/Windows/Mac
- Python 3
- Google Colab
### Dependencies
```python
pip install -r requirements.txt
```
    
# Getting-Started
### Training and Inference
Run the [model.py](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/model.py) or [model.ipynb](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/model.ipynb) to start the training and testing process. The result will give output files of [ICU_model.h5](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/tree/main/Models) and a lite version [model_tflite](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/tree/main/Models).
```python
python model.py
```
# Demo
### Earth
![alt text](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Dataset/Test/Earth/BIRDS-3_Mongolia-1.jpg?raw=true)
### Sun Flare
![alt text](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Dataset/Test/Flare/NanoSat-26.jpg?raw=true)
### Space
![alt text](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/Dataset/Test/Space/D2_MFC_2019-02-27T191956086_%5B000.000%5D-thumb.jpg?raw=true)

# License
This repo is licensed under [MIT License](https://github.com/chandlerbing65nm/Onboard-Satellite-Image-Classification/blob/main/LICENSE)
