from flask import Flask, render_template
import numpy as np

from preditctor import windPowerPredictor

# Create a new web app
app = Flask(__name__)

# Add home route
@app.route("/")
def home():
   return render_template('home.html')

# Add predict route
@app.route('/api/predict/<speed>',methods=['GET'])
def predict(speed):
  return windPowerPredictor.predict(speed)

app.run(debug=True)