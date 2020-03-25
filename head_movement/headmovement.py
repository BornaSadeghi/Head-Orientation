import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import cv2

# Load the model
model = tf.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
cap = cv2.VideoCapture(0)

def classify():
    _, img = cap.read()

    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # crop image
    x,y,w,h = 0,60,640,360
    img = img[y:y+h, x:x+w]

    pilImg = Image.fromarray(img)

    # fit image to 224 by 224 square
    img = ImageOps.fit(pilImg, (224,224), Image.ANTIALIAS)
    img = np.array(img)
    img = cv2.flip(img, 1)

    cv2.imshow("webcam", img)

    # Normalize the image
    normalized_image_array = (img.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    prediction = model.predict(data)
    return np.argmax(prediction)

def getHeadOrientation():
    pos = classify()
    if pos == 1:
        return "up"
    elif pos == 2:
        return "down"
    elif pos == 3:
        return "left"
    elif pos == 4:
        return "right"
    else:
        return "none"