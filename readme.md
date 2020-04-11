# Covid-19 X-ray Classifier



## PROJECT OVERVIEW

A web app to run an image classifier to distinct between covid-19 xrays versus normal. Convolutional Neural Network was built with Keras with Tensorflow backend. 

[Kaggle Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)

## Run with Docker

With **[Docker](https://www.docker.com)**, you can quickly build and run the entire application in minutes :whale:

```shell
- Clone this repo 
$ cd COVID-19-Classification

# 2. Build Docker image
$ docker-compose build

# 3. Run!
$ docker-compose up
```

Open http://localhost:5000 and wait till the webpage is loaded.


## Run locally

- Clone this repo 
- Install requirements
- gunicorn -k gevent -w 5 app:app
- Go to http://localhost
- Done! :tada:

:point_down: Screenshot:

<p align="center">
  <img src="https://user-images.githubusercontent.com/5097752/71063354-8caa1d00-213a-11ea-86eb-879238887c1f.png" height="480px" alt="">
</p>



## TOOLS, MODULES & TECHNIQUES:


##### Python – web development:
Flask 
##### Python – CNN:
keras | tensorflow | scikit-image | pandas | numpy | h5py
##### Web Development:
HTML | CSS | Bootstrap | Materialize


##### References:
1) [Deploy Keras Model with Flask as Web App in 10 Minutes]  (https://github.com/mtobeiyf/keras-flask-deploy-webapp)
2) [Detecting COVID-19 in X-ray images with Keras, TensorFlow, and Deep Learning](https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/)
3) [Open database of COVID-19 cases with chest X-ray or CT images](https://github.com/ieee8023/covid-chestxray-dataset)
