import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn as sk
import random
import tensorflow as tf
import joblib

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import Input
from tensorflow import keras



# Import Database
df = pd.read_csv('../data/raw/5000_car_dataset_TRANSMISSION_FIXED_FINAL.csv')

SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)
random.seed(SEED)
df.info()
df["Power_Weight"] = df["Horsepower"] / df["Weight"]
df["Torque_Weight"] = df["Torque"] / df["Weight"]


# One-Hot Encoding
df_encoded = pd.get_dummies(
    df, 
    columns=['Drivetrain', 'Transmission'],
    drop_first=True,
    dtype=int
)
df_encoded.info()


# Feature Selection
Numerical_features = [
    "Year", 
    "Horsepower", 
    "Engine_Size", 
    "Torque",
    "Power_Weight", 
    "Torque_Weight",
    "Weight",
]

Binary_features = [
    'Drivetrain_RWD',
    'Transmission_DCT',  
]


# Feature Combination
features = Numerical_features + Binary_features
X = df_encoded[features].values
y = df_encoded["Acceleration_0_100"].values

print("Columns in df_encoded:")
print(df_encoded.columns.tolist())
print("\n")
print("Chosen Features:")
print(features)


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, 
    random_state=42
)

numerical_indexes = [features.index(f) for f in Numerical_features]
binary_indexes = [features.index(f) for f in Binary_features]

X_train_numerical= X_train[:,numerical_indexes]
X_train_binary = X_train[:,binary_indexes]

X_test_numerical= X_test[:,numerical_indexes]
X_test_binary = X_test[:,binary_indexes]


# Scaling/Normalization
scaler = StandardScaler()

X_train_scaled_numerical = scaler.fit_transform(X_train_numerical)
X_test_scaled_numercial  = scaler.transform(X_test_numerical)

X_train = np.concatenate([X_train_scaled_numerical,X_train_binary], axis = 1 )
X_test = np.concatenate([X_test_scaled_numercial,X_test_binary], axis = 1 )

# Build Neural Network
model = Sequential([
    Input(shape=(X_train.shape[1],)), 
    
    Dense(64, activation='relu'), 
    Dropout(0.1),

    Dense(64, activation='relu'),
    Dropout(0.1),

    Dense(32, activation='relu'),

    Dense(1)  
])
# added momentum since we kept detecting oscillation
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.00005,
                                    momentum=0.9,
                                    clipnorm=1.0),
    loss='mse',
    metrics=['mae']
)
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=20,
    restore_best_weights=True
)
history = model.fit(
    X_train,
    y_train,
    epochs=200,
    batch_size=128,
    validation_split=0.2,
    callbacks=[early_stop],
    shuffle=True
)

# Save Model (for live prediction and later evaluation)
model.save('../models/nn_zero_to_sixty.keras')
joblib.dump(features, '../models/feature_names.pkl')
joblib.dump(scaler, '../models/nn_scaler.pkl')



# Save Feature Info (for selective scaling)
feature_info = {
    'numeric_features': Numerical_features,
    'binary_features': Binary_features,
    'numeric_indices': [features.index(f) for f in Numerical_features],
    'binary_indices': [features.index(f) for f in Binary_features],
    'total_features': len(features)
}
joblib.dump(feature_info, '../models/feature_info.pkl')


# Correlation with Target
print("Correlation with Acceleration_0_100:")

# Numeric Features
for feat in Numerical_features:
    corr = df_encoded[feat].corr(df_encoded['Acceleration_0_100'])
    print(f"{feat:25s}: {corr:+.4f}")

# Binary Features
for feat in Binary_features:
    corr = df_encoded[feat].corr(df_encoded['Acceleration_0_100'])
    print(f"{feat:25s}: {corr:+.4f}")

model = keras.models.load_model(
    '../models/nn_zero_to_sixty.keras',
    compile=True
)
model.compile(optimizer='rmsprop', loss='mse')
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

test_results = model.evaluate(X_test, y_test, verbose=1)

test_loss = test_results[0]
test_mae = test_results[1] 

print(f"Test Loss (MSE): {test_loss:.4f}")
print(f"Test MAE: {test_mae:.4f}")
print(f"Test RMSE: {np.sqrt(test_loss):.4f}")

