#!/usr/bin/env python
# coding: utf-8

# In[3]:


from keras.layers import Input, Dense
from keras.models import Model
from keras.datasets import mnist
import numpy as np


(x_train, _), (x_test, _) = mnist.load_data()



input_img = Input(shape=(784,))

encoded = Dense(32, activation='relu')(input_img)

decoded = Dense(784, activation='sigmoid')(encoded)

autoencoder = Model(input_img, decoded)

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.summary()


x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
print(x_train.shape)
print(x_test.shape)

n_epochs = 10
autoencoder.fit(x_train, x_train,
                epochs=n_epochs,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))



decoded_imgs = autoencoder.predict(x_test)

import matplotlib.pyplot as plt


# In[4]:



n = 10 
plt.figure(figsize=(20, 4))
for i in range(n):
    ax = plt.subplot(2,n, i+1 )
    plt.imshow(x_test[i].reshape(28, 28))
    #plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(2, n, i + 1+n )
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    #plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()


# In[ ]:





# In[ ]:




