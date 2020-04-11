# import the necessary packages

import os
import io

# Flask
from flask import Flask, render_template, url_for, request, jsonify

#  TensorFlow and Keras 
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import load_model
from keras.layers import Input
from keras.applications import imagenet_utils
from keras.applications import VGG16
from keras.backend import set_session
import tensorflow as tf

# Utilities
import numpy as np
from PIL import Image
from utils import base64_to_pil

# Model saved with Keras model.save()
MODEL_DIR = './models'


# initialize our Flask application and the Keras model
app = Flask(__name__)


session = tf.Session()
set_session(session)


model = load_model(os.path.join(MODEL_DIR,'model_new.h5'))
model._make_predict_function()         
print('Model loaded. Start serving...')


def prepare_image(img):
	# resizing 
	# mean subtraction and scaling
	# img = load_img(imagePath,target_size=(224,224))
	if img.mode != "RGB":
		img = img.convert("RGB")
	img = img.resize((224,224))
	img = img_to_array(img)
	img = np.expand_dims(img, axis=0)
	img=  preprocess_input(img)
	return img


def model_predict(image, model):
	# classify the input image and then initialize the list
	# of predictions to return to the client
	with session.as_default():
		with session.graph.as_default():
			preds = model.predict(image)
			predIdxs = np.argmax(preds, axis=1)
			labels = ['covid-19', 'normal']
			preds = labels[predIdxs[0]]
	return preds



@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route("/predict", methods=["GET", "POST"])
# POST method(enabling us to send arbitrary image, json, etc)
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if request.method == "POST":
		# read the image in PIL format
		image = base64_to_pil(request.json)
		# preprocess the image and prepare it for classification
		image = prepare_image(image)

		data["predictions"] = model_predict(image, model)

		# indicate that the request was a success
		data["success"] = True
		# return the data dictionary as a JSON response

		result = data["predictions"] 
		return jsonify(result=result)
	return None		

# first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	app.run(debug=False, port=5000)
	#to run locally --> curl -X POST -F image=@cov_neg.jpeg 'http://localhost:5000/predict'