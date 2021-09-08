#!/usr/bin/env python
# coding: utf-8

# # Import the important packages

# In[1]:


import numpy as np
from PIL import Image
import os

import matplotlib.pylab as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping


# # Load the dataset

# In[2]:


#print the number of images per folder in our dataset

print('The number of training Earth images: ', len(os.listdir('Dataset/Train/Earth/')))
print('The number of training Flare images: ', len(os.listdir('Dataset/Train/Flare/')))
print('The number of training Space images: ', len(os.listdir('Dataset/Train/Space/')))
print('Total: ', len(os.listdir('Dataset/Train/Earth/')) + len(os.listdir('Dataset/Train/Flare/')) + len(os.listdir('Dataset/Train/Space/')))

print('\nThe number of validation Earth images: ', len(os.listdir('Dataset/Test/Earth/')))
print('The number of validation Flare images: ', len(os.listdir('Dataset/Test/Flare/')))
print('The number of validation Space images: ', len(os.listdir('Dataset/Test/Space/')))
print('Total: ', len(os.listdir('Dataset/Test/Earth/')) + len(os.listdir('Dataset/Test/Flare/')) + len(os.listdir('Dataset/Test/Space/')))


# # Perform data augmention

# In[3]:


TRAINING_DIR = 'Dataset/Train/'
train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=180,
      horizontal_flip=True,
      fill_mode='nearest')
train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                                                    batch_size=5,
                                                    class_mode='categorical',
                                                    target_size=(32, 32)) 

VALIDATION_DIR = 'Dataset/Test/'
validation_datagen = ImageDataGenerator( rescale = 1.0/255. )
validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR,
                                                    batch_size=2,
                                                    class_mode='categorical',
                                                    target_size=(32, 32)) 


# # Load the pretrained model

# In[4]:


pretrained_model = keras.models.load_model('Models\pretrained.h5')

print(pretrained_model.summary())


# # Change the softmax to three classes

# In[5]:


base_outputs = pretrained_model.layers[-6].output
x = layers.Dense(128, activation='relu', name='dense_2')(base_outputs)
x = layers.Dense(3, activation='softmax', name='softmax')(x)

model = keras.Model(inputs = pretrained_model.input, outputs = x)
   
print(model.summary())


# # Using callback for early stopping

# In[6]:


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > 0.98):
            print("\nReached 98% accuracy so cancelling training!\n")
            self.model.stop_training = True

callbacks = myCallback()


# # Train the model

# In[7]:


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_generator,
                    steps_per_epoch = 6,
                    epochs=100,
                    verbose=1,
                    validation_data=validation_generator,
                    callbacks=[EarlyStopping(
                        patience=20,
                        mode='min',
                        monitor='val_loss',
                        restore_best_weights=True,
                        verbose=1)
                              ])


# # Visualize the training and Testing histories

# In[8]:


acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training')
plt.plot(epochs, val_acc, 'b', label='Validation')
plt.title('ACCURACY')
plt.ylabel('metric')
plt.xlabel('# of epochs')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'r', label='Training')
plt.plot(epochs, val_loss, 'b', label='Validation')
plt.title('LOSS')
plt.ylabel('metric')
plt.xlabel('# of epochs')
plt.legend()

plt.show()


# # Save and Load the model

# In[9]:


model.save('Models\ICU_model.h5')

loaded_model = keras.models.load_model('Models\ICU_model.h5')


# # Validate the model using external images

# In[10]:


Sample = Image.open("Testing\Flare\Flare2.jpg").resize((1024, 1024))
Sample.show()


# In[11]:


Sample = Image.open("Testing\Flare\Flare2.jpg").resize((32,32));
Sample = np.array(Sample)/255.0;
Sample.shape;
Sample[np.newaxis, ...];
result = loaded_model.predict(Sample[np.newaxis, ...]);
predicted_label_index = np.argmax(result);
image_labels = []
with open("Dataset_Labels.txt", "r") as f:
    image_labels = f.read().splitlines()
image_labels[:3]

image_labels[predicted_label_index]


# # Convert the model to Tensorflow lite

# In[12]:


converter = converter = tf.lite.TFLiteConverter.from_keras_model(loaded_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
open("Models\model_tflite", "wb").write(tflite_quant_model)


# In[ ]:




