from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('mode.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)
    output = round(prediction[0], 2)

    if output> 5:
        return render_template('index.html', pred='Wine Quality is Good 🤩')
    else:
        return render_template('index.html', pred='Oops! Wine Quality is poor 😥')


if __name__ == '__main__':
    app.run(debug=True)
