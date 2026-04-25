import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout

df = pd.read_csv("data/box_angles.csv", encoding='utf-8-sig', sep=';')
print(repr(df.columns.tolist()))

# classok szamma alakitasa
label_encoder = LabelEncoder()
df['class_encoded'] = label_encoder.fit_transform(df['class'])
NUM_CLASSES = len(label_encoder.classes_)

win_size = 30
step = 5

X = []
Y = []
cols = ['l_elbow_angle', 'r_elbow_angle', 'l_shoulder_angle', 'r_shoulder_angle']
print(f"Osztályok: {label_encoder.classes_}")
# ablakok
for name, group in df.groupby('class'):


    vals = group[cols].values
    label = group['class_encoded'].values[0]
    for i in range(0, len(vals) - win_size, step):
        window = vals[i: i + win_size]
        X.append(window)
        Y.append(label)

X = np.array(X)
Y = np.array(Y)

# 5. One-Hot Encoding a címkékre (Keras elvárás a többosztályos osztályozáshoz)
Y = to_categorical(Y, num_classes=NUM_CLASSES)

print(f"X: {X.shape}")
print(f"Y: {Y.shape}")

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, random_state=42)


model = Sequential()


model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(win_size, len(cols))))
model.add(MaxPooling1D(pool_size=2))
model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())

# 3. Döntéshozó blokk
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Kimeneti réteg
model.add(Dense(NUM_CLASSES, activation='softmax'))

# Modell fordítása
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

history = model.fit(X_train, Y_train, epochs=40, batch_size=32, validation_data=(X_val, Y_val))

# Modell elmentése
model.save("boxing_model.keras")

# Címkekódoló elmentése is hasznos lesz a teszteléshez
np.save('data/classes.npy', label_encoder.classes_)