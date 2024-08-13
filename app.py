from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model =pickle.load(open('galaxy.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=="POST":
        ra=request.form['ra']
        dec=request.form['dec']
        u=request.form['u']
        g=request.form['g']
        r=request.form['r']
        i=request.form['i']
        z=request.form['z']
        run=request.form['run']
        camcol=request.form['camcol']
        field=request.form['field']
        specobjid=request.form['specobjid']
        redshift=request.form['redshift']
        plate=request.form['plate']
        mjd=request.form['mjd']
        fiberid=request.form['fiberid']

        X_test = [[
            ra,
            dec,
            u,
            g,
            r,
            i,
            z,
            run,
            camcol,
            field,
            specobjid,
            redshift,
            plate,
            mjd,
            fiberid
        ]]
    # Make prediction
    prediction = model.predict(X_test)
    output=prediction[0]
    
    if output==0:
       return render_template('index.html', prediction_text='The object is galaxy')
    
    elif output==1:
        return render_template('index.html', prediction_text='The object is quasar')
    
    elif output==2:
        return render_template('index.html', prediction_text='The object is star')

if __name__ == '__main__':
    app.run(debug=True)
