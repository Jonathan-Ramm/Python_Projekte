import keras, skimage
from keras import layers
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.optimizers import Adam
from skimage.transform import resize
import tensorflow as tf
import tensorflowjs as tfjs

# Laden und Vorverarbeiten
(X_train, Y_train), (X_test, Y_test) = keras.datasets.mnist.load_data()

# Reshape und Normalisierung
X_train = X_train.reshape((X_train.shape[0], 784)).astype('float32') / 255
X_test = X_test.reshape((X_test.shape[0], 784)).astype('float32') / 255

# Erstellen und Trainieren des Modells
model = keras.Sequential(
    [
        keras.Input(shape=(784,)),
        layers.Dense(1024, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)),
        layers.BatchNormalization(), 
        layers.Dropout(0.3), 
        layers.Dense(1024, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)), 
        layers.BatchNormalization(),
        layers.Dropout(0.2),
        layers.Dense(512, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)), 
        layers.BatchNormalization(),
        layers.Dropout(0.2),
        layers.Dense(256, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)), 
        layers.BatchNormalization(),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax') 
    ]
)

# Kompilierung des Modells
model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer=Adam(learning_rate=0.001),  
    metrics=["accuracy"]
)

# Callbacks für verbessertes Training
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
lr_reduction = ReduceLROnPlateau(monitor='val_loss', patience=3, factor=0.5, min_lr=1e-6)

# Modelltraining
history = model.fit(
    X_train,
    Y_train,
    batch_size=64,
    epochs=100, 
    validation_split=0.1,
    callbacks=[early_stopping, lr_reduction]
)

# Speichern der Modellgewichte
model.save_weights('model.weights.h5')
model.save('model.h5')
model.compile(loss="sparse_categorical_crossentropy", optimizer=Adam(learning_rate=0.001), metrics=["accuracy"])



# Lade das Keras-Modell
model = tf.keras.models.load_model('model.h5')

# Konvertiere das Modell in TensorFlow.js Format
tfjs.converters.save_keras_model(model, 'tfjs_model')


loss, accuracy = model.evaluate(X_test, Y_test)
print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

