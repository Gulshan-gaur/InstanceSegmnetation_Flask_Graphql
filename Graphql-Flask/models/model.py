import os 
import joblib
import sys
sys.path.insert(0,'../')
model_path = os.path.join('models/rf_regressor.pkl') 
model = joblib.load(model_path)


def predict(request):
    int_features = [[x for x in request.values()]]
    output = model.predict(int_features)
    return output

