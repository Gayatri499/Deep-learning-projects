from flask import*

import numpy as np
import warnings

from keras.models import load_model
from time import sleep
from keras.models import model_from_json

import tensorflow as tf     

from tensorflow.keras.models import model_from_json


app=Flask(__name__)
@app.route('/')
@app.route('/res',methods=['POST','GET'])
def fun():
    if request.method=="POST":
        a1=int(request.form['a'])
        b1=int(request.form['b'])
        c1=float(request.form['c'])
        d1=float(request.form['d'])
        e1=float(request.form['e'])
        f1=float(request.form['f'])
        g1=float(request.form['g'])
        json_file=open(r'modelsGG.json','r')
        loaded_model_json=json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(r"models1GG.h5")
        features = np.array([[a1,b1,c1,d1,e1,f1,g1]])
        prediction = loaded_model.predict(features)
        if(prediction):
            return render_template("index.html",data="Fraud")
        else:
            return render_template("index.html",data="Not Fraud")
    else:
        return render_template("index.html",data=" ")
    
if __name__=='__main__':
    app.run(debug=True)