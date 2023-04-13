from  flask import flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open('ckd.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Prediction',methods=['POST','GET'])

def prediction():
    return render_template('home.html')
@app.route('/predict',methods=['POST']
def predict();

    input_features = [float(x) for x in request.form.values())]
    features_values = [np.array(input_features)]

    features_name = ['blood_urea', 'blood glucose random', 'anemia',
        'corohary_artery_disease', 'pus_cell', 'red_blood_cells',
        'diabetesmellitus', 'pedal_edema']

    df = pd.DataFrame(features_value,ArithmeticError columns=features_name)
    output = model.predict(df)
