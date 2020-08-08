# Product Service
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import _pickle as pickle
import numpy as np
from sklearn import datasets, linear_model

app = Flask(__name__)
api = Api(app)

#Hello

PickleModelPath = './regressionaggag.pkl'

@app.route('/score')
def apicall():  
    var = float(request.args.get('var1'))
    var1 = np.reshape(var, (-1, 1))
    with open(PickleModelPath, 'rb') as k:
        PickleModel = pickle.load(k)
    Answer = PickleModel.predict(var1)
    return jsonify( Answer.tolist())


@app.route('/train')
def apicalled():
    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()
    # Use only one feature
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]
    # Split the targets into training/testing sets
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)
    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)
    with open(PickleModelPath, 'wb') as f:
            pickle.dump(regr, f)  
    return "Model hase been retrained. Run /score to score model"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5071, debug=False)

#http://localhost:5071/train
#http://localhost:5071/score?var1=10