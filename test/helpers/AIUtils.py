from PIL import Image
import numpy as np
from keras.models import load_model


def predict_from_path(path: str):
    # Preprocess the image
    image = Image.open(path).resize((28, 28)).convert('L')
    data = np.array(image).astype(np.float32)/255
    data = [[item for sublist in data for item in sublist]]
    data = np.array(data).astype(np.float32)
    model = load_model('helpers/digitModel.h5')
    prediction = np.argmax(model.predict(data), axis=-1)
    return prediction[0]