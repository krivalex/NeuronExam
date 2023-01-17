
def predict(data):
  import numpy as np # linear algebra
  import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler
  from tensorflow import keras
  from keras.models import Sequential
  from keras.layers import Dense



  X = data.iloc[:,0:5].values
  Y = data.iloc[:,5].values
  x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=0)



  sc = StandardScaler()
  X_train = sc.fit_transform(x_train)
  X_test = sc.fit_transform(x_test)



  classifier = Sequential()

  # Hidden layers and input layer are  added.
  classifier.add(Dense(3, kernel_initializer="uniform", activation = 'relu', input_dim = 5))

  classifier.add(Dense(3, kernel_initializer="uniform", activation = 'relu'))

  # Output layer
  classifier.add(Dense(1, kernel_initializer="uniform", activation = 'sigmoid'))

  classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

  classifier.fit(X_train, y_train, epochs = 50)

  # Prediction
  y_pred1 = classifier.predict(X_test)

  y_pred2 = (y_pred1 > 0.5)

  from sklearn.metrics import confusion_matrix

  cm = confusion_matrix(y_test, y_pred2)
  return [y_pred1, cm]
