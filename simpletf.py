import tensorflow as tf
import numpy as np

# Generate some random data
num_points = 1000
dimensions = 2

# Labels are either 0 or 1
labels = np.random.randint(2, size=num_points)

# Features are random points in 2D space
features = np.random.rand(num_points, dimensions)

# Split the data into a training set and a test set
split = int(num_points * 0.8)
x_train, x_test = features[:split], features[split:]
y_train, y_test = labels[:split], labels[split:]

# Define the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(dimensions,), activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
accuracy = model.evaluate(x_test, y_test, batch_size=32)[1]
print('Test accuracy: %.2f' % accuracy)
