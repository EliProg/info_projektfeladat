import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import csv
import os
import numpy as np


def extract_coord(video, name, output):
    # fejlec
    if not os.path.exists(output):
        landmarks = ['class', 'frame_id']
        for i in range(33):
            landmarks += [f'x{i}', f'y{i}', f'z{i}', f'v{i}']

        with open(output, mode='w', newline='') as f:
            cw = csv.writer(f, delimiter=';')
            cw.writerow(landmarks)


    # video megnyitas
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print(f"Hiba: Nem sikerült megnyitni a videót: {video}")
        return

  # fps lekeres, 30 fps failsafe
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30.0  #

    #
    base_options = python.BaseOptions(model_asset_path='data/pose_landmarker_full.task')
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        num_poses=1,
        min_pose_detection_confidence=0.5,
        min_pose_presence_confidence=0.5,
        min_tracking_confidence=0.5
    )

    frame_id = 0

    with vision.PoseLandmarker.create_from_options(options) as landmarker:
        with open(output, mode='a', newline='') as f:
            cw = csv.writer(f, delimiter=';')

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                mp_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

                time_ms = int((frame_id * 1000) / fps)

                detection_result = landmarker.detect_for_video(mp_frame, time_ms)
                if detection_result.pose_landmarks:

                    first_person_landmarks = detection_result.pose_landmarks[0]
                    pose_row = list(np.array([[lm.x, lm.y, lm.z, lm.visibility]
                                              for lm in first_person_landmarks]).flatten())

                    row = [name, frame_id] + pose_row
                    cw.writerow(row)

                frame_id += 1

    cap.release()

extract_coord("videok/stance.mp4", "stance", "data/box_koordinatak.csv")
extract_coord("videok/left_straight_100.mp4", "straight", "data/box_koordinatak.csv")
extract_coord("videok/right_straight_100.mp4", "straight", "data/box_koordinatak.csv")
extract_coord("videok/left_hook_100.mp4", "hook", "data/box_koordinatak.csv")
extract_coord("videok/right_hook_100.mp4", "hook", "data/box_koordinatak.csv")
extract_coord("videok/left_uppercut_100.mp4", "uppercut", "data/box_koordinatak.csv")
extract_coord("videok/right_uppercut_100.mp4", "uppercut", "data/box_koordinatak.csv")


