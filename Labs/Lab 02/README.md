# Lab 02 - The basics of serialisation in Python

Welcome to Lab 02 here we will look very quickly at the basics of using pickle. Hope we have looked at this in the slides. And we have seen what Pickle is used for. We will be using Pickle to take the model we create and serialise a version of it to our local file system. 

Lets begin by looking at a super simple example from the Pickle wiki. 

## Step 1 

If you have not used pickle before then you will need to import the library. 

```
python -m pip install pickle
```

Once installed you can execute the following lines of python in jupyter. 

```
import pickle
```
Pickle example

```
favorite_color = { "lion": "yellow", "kitty": "red" }
print(favorite_color)
pickle.dump( favorite_color, open( "save.p", "wb" ) )
favorite_color_pickle = pickle.load( open( "save.p", "rb" ) )
print(favorite_color_pickle)
```

If you open save.p you will see the serialised version of that model. 

## Step 2

In this step we will pickle the output of our model and then score using it.

```
import _pickle as pickle
import numpy as np
from sklearn import datasets, linear_model

PickleModelPath = './regression.pkl'

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_pred = regr.predict(diabetes_X_test)
with open(PickleModelPath, 'wb') as f:
        pickle.dump(regr, f)  
```

If you navigate to where regression.pkl was created you can see the serialised version of the model. 

## Step 3 

Create a new python notebook, but this time do not import the same libaries as before. 

Just run the following. 

```
import _pickle as pickle

PickleModelPath = './regression.pkl'

var1 = 10

with open(PickleModelPath, 'rb') as k:
        PickleModel = pickle.load(k)
Answer = PickleModel.predict(var1)

print(Answer)
```
We are now able to score our model without the need to import SKlearn. 

We can also store this model in source control. 