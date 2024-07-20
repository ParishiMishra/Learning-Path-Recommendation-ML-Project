import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras import Dense, InputLayer
from syndata import *

X = df[['quiz_scores', 'assignment_completion', 'time_spent_on_tasks', 'frequency_of_interactions', 'emotional_state']].values
y = df['average_performance'].values

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Build the deep reinforcement learning model
model = Sequential()
model.add(InputLayer(input_shape=(X_scaled.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer='adam', loss='mse')
model.summary()

# Train the model
model.fit(X_scaled, y, epochs=50, batch_size=10, validation_split=0.2)