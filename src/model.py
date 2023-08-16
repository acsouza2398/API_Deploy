import pickle

def load_model():
    model = pickle.load(open('../models/model.pkl', 'rb'))
    return model


def load_encoder():
    encoder = pickle.load(open('../models/ohe.pkl', 'rb'))
    return encoder