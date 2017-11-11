from os import path
import sys

import cv2
import pandas as pd

from src.preprocessing import preprocessing
from src.pytess import recognize_text
from src.metrics import text_recognition_score

OBJECT_NAME = 'pricetag'
IMAGES_DIR = 'data/crop_images_' + OBJECT_NAME + '/'
METADATA_DIR = 'data/csv/'
METADATA = 'df_crop_' + OBJECT_NAME

df_metadata = pd.read_csv(path.join(sys.path[1], METADATA_DIR, METADATA))

image_names = df_metadata['filename'].tolist()

result = []

for image_name in image_names:

    image = cv2.imread(path.join(sys.path[1], IMAGES_DIR, image_name))
    image = preprocessing(image=image)

    predicted_text = recognize_text(image=image)
    target_text = df_metadata[df_metadata['filename'] == image_name]['attribute'].tolist()[0]

    score = text_recognition_score(target_text=target_text, predicted_text=predicted_text)

    result.append([image_name, target_text, predicted_text, score[0], score[1]])

df_result = pd.DataFrame(data=result, columns=['filename',
                                               'target_text',
                                               'predicted_text',
                                               'ratio',
                                               'jaro_winkler'])

df_result.to_csv(path.join(sys.path[1], METADATA_DIR, 'result' + OBJECT_NAME))
