from flask import *
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import traceback

import tensorflow as tf
import cv2
import os
import numpy as np

import openai
import gradio

model = tf.keras.models.load_model("image_to_recipie_model.h5")


category={
    0: ['Apple Pie'], 1: ['Baklava'], 2: ['Burger'],
    3: ['Burrito'], 4: ['Chappati'], 5: ['Cheese Plate'],
    6: ['Chole Bhature'], 7: ['Creme Brulee'], 8: ['Cup Cakes'], 9: ['Dal'],
    10: ['Dhohkla'], 11: ['Donuts'], 12: ['French Fries'],
    13: ['Fried Rice'], 14: ['Ice Cream'], 15: ['Kofta'],
    16: ['Lasagna'], 17: ['Macaroni and Cheese'], 18: ['Macaroons'], 19: ['Nachos'],20:['Pakora'],21:['Panner Butter Masala'],
    22:['Pav Bhaji']
    ,23:['Pizza',],24:['Ramen',],25:['Samosa'],26:['Spaghetti Carbonara'],27:['Spring Roll'],28:['Tiramisu'],29:['Tuna Tarrtare'],30:['Vadapav'],31:['Waffles']
}


def chatGPT(text):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"Give me the recipie of {text} in india"}])
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


def prediction(filename,model):
    img_ = image.load_img(filename, target_size=(299, 299))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255.

    prediction = model.predict(img_processed)

    index = np.argmax(prediction)

    return render_template('/uploadimage.html',result="It is an image of "+(category[index][0]),text=chatGPT(category[index][0]),heading="Recpie of "+(category[index][0]))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/uploadimage')
def main():
    return render_template('/uploadimage.html')


@app.route('/Image')
def Image():
    return render_template("/image.html")

@app.route('/Burger')
def Burger():
    return render_template("/Burger.html")

@app.route('/ButterChicken')
def ButterChicken():
    return render_template("/ButterChicken.html")

@app.route('/Cherry')
def Cherry():
    return render_template("/Cherry.html")

@app.route('/Corn')
def Corn():
    return render_template("/Corn.html")


@app.route('/Dosa')
def Dosa():
    return render_template("/Dosa.html")


@app.route('/FrenchFries')
def FrenchFries():
    return render_template("/FrenchFries.html")


@app.route('/Grapes')
def Grapes():
    return render_template("/Grapes.html")


@app.route('/KadhiPaneer')
def KadhiPaneer():
    return render_template("/KadhiPaneer.html")


@app.route('/Lazania')
def Lazania():
    return render_template("/Lazania.html")


@app.route('/momos')
def momos():
    return render_template("/momos.html")


@app.route('/Pancake')
def Pancake():
    return render_template("/Pancake.html")

@app.route('/Pizza')
def Pizza():
    return render_template("/Pizza.html")


@app.route('/', methods=['POST'])
def third():
    try:
        if 'file' in request.files and request.files['file'] and request.files['file'].filename != '':
            s=""
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(filename)
            result = prediction(filename,model)
            os.remove(filename)
            
            return result
        else:
            return render_template('/uploadimage.html',heading="File Not found")
    except Exception:
        print(traceback.format_exc())
        return render_template('/uploadimage.html',heading="Error 404")


if __name__ == "__main__":
    app.run(debug=True)