# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:55:07 2020

@author: Chirag
"""
''' Real Time Prediction '''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

# Importing the model Which is trained on Sign Language Detection dataset.
bring_model = tf.keras.models.load_model("main_model_12e.h5")

def get_alpha(val):
    names = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'DEL': 26, 'NOTHING': 27, 'SPACE': 28}
    for key, value in names.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

''' Imp NOTE :- Press Q button in order to close the windoe of the WebCam '''
def capture_pic():
    
    cap = cv2.VideoCapture(0)
    
    while (True):
        
        ret, frame = cap.read()
        
        cv2.imshow("Video", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Showing the image which is captured by the WebCam.
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame)
    plt.xticks([])
    plt.yticks([])
    plt.title('Captured image')
    plt.show()
    
    cv2.imwrite("Test.jpg", frame)
    
    return frame

frame = capture_pic()
image = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) / 255.0

y_pred = bring_model.predict(image.reshape((1, ) + image.shape))
val = np.argmax(y_pred)

Alphabet_pred = get_alpha(val)
print(Alphabet_pred)


