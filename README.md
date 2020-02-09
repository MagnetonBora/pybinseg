# Segmentation app

This is a simple web application developed during the studying at MIPT [deep learning school](https://www.dlschool.org/).

## About neural network

A neural network created during this project has been taken from [this](https://github.com/qubvel/segmentation_models/blob/master/examples/binary%20segmentation%20(camvid).ipynb) example notebook. 

## About the dataset

The dataset for neural network training has been taken from [this](https://github.com/alexgkendall/SegNet-Tutorial/tree/master/CamVid) dataset.

## Deploy on heroku

The easiest way to run the app is to run it on Heroku. Just click this button 👉 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MagnetonBora/pybinseg)

Of course, you need to have an account on [Heroku](https://www.heroku.com/).

## Deploy locally

If you need to run the app locally do the following.

1. Clone the repo.
2. Create virtual env `mkvirtualenv pybinseg -p python 3`
3. Install requirements `pip install -r requirements.txt`
4. Run the app `python main.py` or `gunicorn main:app`
