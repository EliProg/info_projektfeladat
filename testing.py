import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import coordinates
import angles

test_vid = "videok/test.mp4"
output = "data/result.txt"

coordinates.extract_coord(test_vid, "teszt", "data/teszt_koordinatak.csv")

angles.extract_angl("data/teszt_koordinatak.csv", "data/teszt_angles.csv")
model = load_model("data/boxing_model.keras")
classes = np.load("data/classes.npy", allow_pickle=True)

df = pd.read_csv("data/teszt_angles.csv", sep=';')
cols = ['l_elbow_angle', 'r_elbow_angle', 'l_shoulder_angle', 'r_shoulder_angle']
angl_vals = df[cols].values

win_size = 30
step = 5

matches = []

for i in range(0, len(angl_vals) - win_size, step):
    window = angl_vals[i: i + win_size]

    l_elbow_std = np.std(window[:, 0])
    r_elbow_std = np.std(window[:, 1])

    if l_elbow_std > 5.0 or r_elbow_std > 5.0:
        input_data = np.expand_dims(window, axis=0)
        prediction = model.predict(input_data, verbose=0)
        class_idx = np.argmax(prediction)
        confidence = prediction[0][class_idx]

        if confidence > 0.85:
            fps = 30
            frame_id = df['frame_id'].values[i + win_size]
            ido_mp = frame_id / fps
            matches.append((ido_mp, frame_id, classes[class_idx], confidence))


with open(output, "w", encoding="utf-8") as f:
    f.write(f"Videó: {test_vid}\n")
    f.write("-" * 35 + "\n\n")

    for ido, frame, mozgas, conf in matches:
        sor = f"[{ido:05.2f}s] (Frame: {frame:04d}) - {mozgas.upper()} ({conf*100:.1f}%)\n"
        f.write(sor)
        print(sor, end="")

print(output)