import pandas as pd
import numpy as np

def vectorise(A, B, C):

    # A = vall, B = konyok, C = csuklo

    a = A.to_numpy()
    b = B.to_numpy()
    c = C.to_numpy()

    ba = a - b
    bc = c - b
    #vektorhossz
    norm_ba = np.linalg.norm(ba, axis=1)
    norm_bc = np.linalg.norm(bc, axis=1)

    # skalaris
    dot = np.sum(ba * bc, axis=1)

    # cos tetel
    cosine = dot / (norm_ba * norm_bc)

    cosine = np.clip(cosine, -1.0, 1.0)

    return np.degrees(np.arccos(cosine))


def extract_angl(input_csv, output_csv):

    df = pd.read_csv(input_csv, sep=None, engine='python', encoding='utf-8-sig')
    df.columns = df.columns.str.strip()
    df = df.copy()

    def coord(i):
        return df[[f'x{i}', f'y{i}', f'z{i}']]

    l_shoulder = coord(11)
    r_shoulder =  coord(12)
    l_elbow = coord(13)
    r_elbow =  coord(14)
    l_wrist = coord(15)
    r_wrist = coord(16)
    l_hip = coord(23)
    r_hip = coord(24)


    df['l_elbow_angle'] = vectorise(l_shoulder, l_elbow, l_wrist)
    df['r_elbow_angle'] = vectorise(r_shoulder, r_elbow, r_wrist)
    df['l_shoulder_angle'] = vectorise(l_hip, l_shoulder, l_elbow)
    df['r_shoulder_angle'] = vectorise(r_hip, r_shoulder, r_elbow)




    angles = df[['class', 'frame_id',
                      'l_elbow_angle', 'r_elbow_angle',
                      'l_shoulder_angle', 'r_shoulder_angle']]

    angles.to_csv(output_csv, index=False, sep=';')


# extract_angl("data/box_koordinatak.csv", "data/box_angles.csv")