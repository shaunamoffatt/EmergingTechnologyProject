# Un comment for code to work in VS Code
#import keras
#from keras.models import load_model
import numpy as np
from flask import request, jsonify, render_template, Flask
from tensorflow.keras.models import load_model
class WindPowerPredictor:
    
    def __init__(self):
            self.model = load_model('model.h5')
    
    def predict(self, speed):
        speed = float(speed)
        if speed < 0:
            return "Wind Speed must be bigger than 0"
        elif speed > 25:
                return "0"
        else:
            speed = np.array([speed])
            prediction = self.model.predict(speed)
            print(prediction)
            return str(prediction)

windPowerPredictor = WindPowerPredictor()