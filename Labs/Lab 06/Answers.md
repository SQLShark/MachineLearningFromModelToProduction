# Answers 

You cheat! I am just kidding. It is complicated. 

Let's walk though the solution end-to-end.

## Step 1

Create the following files: 
```
Dockerfile
app.py
requirements.txt
```

in the Dockerfile we will want to add the following: 

```
FROM python:3-onbuild
COPY . usr/src/app
CMD ["python", "DiabetesModelFlask.py"]
```

in app.py we want to add the following: 

```
# Product Service
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import _pickle as pickle
import numpy as np
from sklearn import datasets, linear_model

app = Flask(__name__)
api = Api(app)

PickleModelPath = './regression.pkl'

@app.route('/score')
def apicall():  
    var1 = float(request.args.get('var1'))
    with open(PickleModelPath, 'rb') as k:
        PickleModel = pickle.load(k)
    Answer = PickleModel.predict(var1)
    return jsonify(Answer.tolist())


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
    app.run(host='0.0.0.0', port=5071, debug=True)
```

Now our requirements is slightly more difficult. We have a lot mode modules which need to be added. 

```
pandas
sklearn
numpy
scipy
Flask==0.12
flask_restful==0.3.5
```

## Step 2

Navigate to the location of your docker file.

For me that looks like this
```
G:

cd G:\GitHubProjects\workshop-ModelManagement\MachineLearningFromModelToProduction\Docker\DockerFlaskModel
```

We will want to build our model 

```
docker build -t diabetesproduction .
```

This will be build our image. 

```
docker run --name diabetes -p 5071:5071 diabetesproduction
```

Now navigate to localhost:5071 and you will see an error. 
That is because part of our web service is missing. If you train the model first you will be able to execute the model. 

```
localhost:5071/train?var1=1
localhost:5071/score?var1=1
```

Lab done.