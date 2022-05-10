import cv2
import mediapipe as mp
import os
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils

FILES_PATH = "/data/Numbers.v7i.yolov5pytorch/test/images/"
removed_path = "/data/Numbers.v7i.yolov5pytorch_pose_detection/test/images/"
if not os.path.exists(removed_path):
    # Create a new directory because it does not exist
    os.makedirs(removed_path)
    print("{} directory was created".format(removed_path))
else:
    print("{} directory already exists".format(removed_path))
directory = os.fsencode(FILES_PATH)
IMAGE_FILES = {}

for file in os.listdir(directory):
    filename = str(os.path.basename(file))
    filename = filename[2:]
    filename = filename[:-1]
    if filename.endswith('.jpg'):
        IMAGE_FILES[FILES_PATH + filename] = filename

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    for idx, file in enumerate(list(IMAGE_FILES.keys())):
        #         print(file)
        bg_image = None
        image = cv2.imread(file)

        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        cv2.imwrite(removed_path + IMAGE_FILES[os.path.abspath(file)], image)




