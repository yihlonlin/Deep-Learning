#!/usr/bin/env python
# coding: utf-8

# In[14]:


# example of using the upsampling layer
from numpy import asarray
from keras.models import Sequential
from keras.layers import UpSampling2D, MaxPooling2D

# define input data
X = asarray([[1, 1, 2, 2],
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]])
# show input data for context
print(X)
# reshape input data into one sample a sample with a channel
X = X.reshape((1, 4, 4, 1))
# define model
model = Sequential()
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), input_shape=(4, 4, 1)))
model.summary()
# make a prediction with the model
yhat = model.predict(X)
# reshape output to remove channel to make printing easier
yhat = yhat.reshape((2, 2))
# summarize output
print(yhat)


# In[15]:


# example of using the upsampling layer
from numpy import asarray
from keras.models import Sequential
from keras.layers import UpSampling2D
# define input data
X = asarray([[1, 2],
			 [3, 4]])
# show input data for context
print(X)
# reshape input data into one sample a sample with a channel
X = X.reshape((1, 2, 2, 1))
# define model
model = Sequential()
model.add(UpSampling2D(input_shape=(2, 2, 1)))
# summarize the model
model.summary()
# make a prediction with the model
yhat = model.predict(X)
# reshape output to remove channel to make printing easier
yhat = yhat.reshape((4, 4))
# summarize output
print(yhat)


# In[ ]:





# In[ ]:




