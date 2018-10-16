# Import the required libaraies 
import _pickle as pickle

PickleModelPath = './regression.pkl'

var1 = 10

with open(PickleModelPath, 'rb') as k:
        PickleModel = pickle.load(k)
Answer = PickleModel.predict(var1)

print(Answer)

