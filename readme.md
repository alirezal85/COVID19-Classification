# COVID-19 X-ray Classifier

## Disclaimer: This app is built only for educational purposes and not suitable to use in the real world whatsoever!

## Project Overview

A web app to run an image classifier to distinct between COVID-19 Xrays versus normal[1]. The model is based on the Convolutional Neural Network built with Keras with Tensorflow backend[2].
Datasets: [3-4]



## Run with Docker :whale:

```shell
- Clone this repo 
$ cd COVID19-Classification

# 2. Build Docker image
$ docker-compose build

# 3. Run!
$ docker-compose up
```

Open http://localhost and wait till the webpage is loaded.


## Run locally

- Clone this repo 
- Install requirements
- gunicorn -k gevent -w 5 app:app -b 0.0.0.0:5000
- Go to http://localhost:5000
- Done! :tada:

:point_down: Screenshot:

<p align="center">
  <img src="/screenshots/screenshot_image.png" height="480px" alt="">
</p>



## Tools and Modules


##### Python – web development:
Flask 
##### Python – CNN:
keras | tensorflow | scikit-image | pandas | numpy | h5py
##### Web Development:
HTML | CSS | JS


##### References:
1) [Deploy Keras Model with Flask as Web App in 10 Minutes](https://github.com/mtobeiyf/keras-flask-deploy-webapp)
2) [Detecting COVID-19 in X-ray images with Keras, TensorFlow, and Deep Learning](https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/)
3) [Open database of COVID-19 cases with chest X-ray or CT images](https://github.com/ieee8023/covid-chestxray-dataset)
4) [X-ray images for healthy individuals](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
